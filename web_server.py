import os
import json
import time
from datetime import datetime
from flask import Flask, jsonify, render_template
from utils.db import get_conn
from utils.realms import get_realm_index
from flask import request

app = Flask(__name__)


def format_timestamp(timestamp):
    """Convert Unix timestamp to readable format"""
    if not timestamp:
        return "N/A"
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")


def format_remaining_years(seconds):
    """Convert remaining seconds to cultivation years (2 decimal places)."""
    if not seconds or seconds <= 0:
        return "-"
    years = seconds / (2 * 3600)
    return f"{years:.2f} 年"


def get_all_players():
    """Fetch all players from database"""
    with get_conn() as conn:
        rows = conn.execute("""
            SELECT 
                discord_id, name, gender, spirit_root, spirit_root_type,
                comprehension, physique, fortune, bone, soul,
                lifespan, lifespan_max, cultivation, realm,
                spirit_stones, reputation, created_at, last_active,
                cultivating_until, cultivating_years,
                is_dead, rebirth_count, is_virgin, sect, sect_rank,
                techniques, current_city, explore_count, cave,
                discovered_sects, escape_rate, has_bahongchen
            FROM players
            ORDER BY cultivation DESC
        """).fetchall()
    
    players = []
    now = time.time()
    for row in rows:
        player = dict(row)
        # Parse JSON fields
        try:
            player['techniques'] = json.loads(player['techniques'] or '[]')
        except:
            player['techniques'] = []
        
        try:
            player['discovered_sects'] = json.loads(player['discovered_sects'] or '[]')
        except:
            player['discovered_sects'] = []
        
        # Format timestamps
        player['created_at_formatted'] = format_timestamp(player['created_at'])
        player['last_active_formatted'] = format_timestamp(player['last_active'])
        
        # Calculate realm rank
        player['realm_index'] = get_realm_index(player['realm'])
        
        # Status
        player['status'] = '已坐化' if player['is_dead'] else '健在'

        # Cultivation/retreat status
        cultivating_until = player.get('cultivating_until')
        cultivating_until_ts = float(cultivating_until) if cultivating_until is not None else 0.0
        is_cultivating = (
            player['is_dead'] == 0
            and cultivating_until is not None
            and cultivating_until_ts > now
        )
        remaining_seconds = (cultivating_until_ts - now) if is_cultivating else 0
        player['cultivating_years_display'] = f"{player['cultivating_years']} 年" if player.get('cultivating_years') else '-'
        player['is_cultivating'] = 1 if is_cultivating else 0
        player['cultivation_status'] = '闭关中' if is_cultivating else '空闲'
        player['retreat_remaining'] = format_remaining_years(remaining_seconds)
        player['cultivating_until_formatted'] = format_timestamp(cultivating_until) if is_cultivating else '-'
        
        players.append(player)
    
    return players


@app.route('/')
def dashboard():
    """Main dashboard page"""
    return render_template('dashboard.html')


@app.route('/api/players')
def api_players():
    """API endpoint to get all players data"""
    try:
        players = get_all_players()
        return jsonify({
            'success': True,
            'total': len(players),
            'players': players
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/quests')
def api_quests():
    """API endpoint to get active quests"""
    try:
        with get_conn() as conn:
            rows = conn.execute("""
                SELECT 
                    name, discord_id, active_quest, quest_due
                FROM players
                WHERE active_quest IS NOT NULL AND is_dead = 0
                ORDER BY quest_due ASC
            """).fetchall()
        
        quests = []
        now = time.time()
        for row in rows:
            player = dict(row)
            try:
                quest_data = json.loads(player['active_quest'])
            except:
                continue
            
            quest_due = player['quest_due']
            remaining = quest_due - now if quest_due and quest_due > now else 0
            is_complete = quest_due and now >= quest_due
            
            quests.append({
                'player_name': player['name'],
                'discord_id': player['discord_id'],
                'quest_id': quest_data.get('id', ''),
                'quest_title': quest_data.get('title', '未知任务'),
                'quest_type': quest_data.get('type', ''),
                'quest_desc': quest_data.get('desc', ''),
                'quest_due': quest_due,
                'quest_due_formatted': format_timestamp(quest_due) if quest_due else '-',
                'remaining_seconds': remaining,
                'remaining_formatted': format_remaining_years(remaining * 2 * 3600) if remaining > 0 else '已完成',
                'is_complete': is_complete,
                'status': '可完成' if is_complete else '进行中'
            })
        
        return jsonify({
            'success': True,
            'total': len(quests),
            'quests': quests
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/stats')
def api_stats():
    """API endpoint to get overall statistics"""
    try:
        with get_conn() as conn:
            # Total players
            total = conn.execute("SELECT COUNT(*) as count FROM players").fetchone()['count']
            
            # Alive players
            alive = conn.execute("SELECT COUNT(*) as count FROM players WHERE is_dead = 0").fetchone()['count']
            
            # Dead players
            dead = conn.execute("SELECT COUNT(*) as count FROM players WHERE is_dead = 1").fetchone()['count']
            
            # Total spirit stones in circulation
            total_stones = conn.execute(
                "SELECT SUM(spirit_stones) as total FROM players WHERE is_dead = 0"
            ).fetchone()['total'] or 0
            
            # Players by sect
            sects = conn.execute("""
                SELECT sect, COUNT(*) as count 
                FROM players 
                WHERE sect IS NOT NULL AND is_dead = 0
                GROUP BY sect
                ORDER BY count DESC
            """).fetchall()
            
            # Players by realm
            realms = conn.execute("""
                SELECT realm, COUNT(*) as count 
                FROM players 
                GROUP BY realm
                ORDER BY count DESC
            """).fetchall()
            
            # Top cultivators
            top_cultivators = conn.execute("""
                SELECT name, realm, cultivation, spirit_stones
                FROM players
                WHERE is_dead = 0
                ORDER BY cultivation DESC
                LIMIT 10
            """).fetchall()
        
        return jsonify({
            'success': True,
            'stats': {
                'total_players': total,
                'alive_players': alive,
                'dead_players': dead,
                'total_spirit_stones': total_stones,
                'sects': [dict(s) for s in sects],
                'realms': [dict(r) for r in realms],
                'top_cultivators': [dict(c) for c in top_cultivators]
            }
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/public_events')
def api_public_events():
    """API endpoint to get all public events with participants"""
    try:
        with get_conn() as conn:
            rows = conn.execute("SELECT * FROM public_events ORDER BY started_at DESC").fetchall()
            events = []
            for event_row in rows:
                event = dict(event_row)
                participants_rows = conn.execute(
                    "SELECT * FROM public_event_participants WHERE event_id = ? ORDER BY joined_at ASC",
                    (event['event_id'],)
                ).fetchall()
                event['participants'] = [dict(p) for p in participants_rows]
                events.append(event)
        return jsonify({
            'success': True,
            'total': len(events),
            'events': events
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


if __name__ == '__main__':
    port = int(os.getenv('WEB_PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)
