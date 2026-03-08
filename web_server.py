import os
import json
from datetime import datetime
from flask import Flask, jsonify, render_template
from utils.db import get_conn
from utils.realms import get_realm_index

app = Flask(__name__)


def format_timestamp(timestamp):
    """Convert Unix timestamp to readable format"""
    if not timestamp:
        return "N/A"
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")


def get_all_players():
    """Fetch all players from database"""
    with get_conn() as conn:
        rows = conn.execute("""
            SELECT 
                discord_id, name, gender, spirit_root, spirit_root_type,
                comprehension, physique, fortune, bone, soul,
                lifespan, lifespan_max, cultivation, realm,
                spirit_stones, reputation, created_at, last_active,
                is_dead, rebirth_count, is_virgin, sect, sect_rank,
                techniques, current_city, explore_count, cave,
                discovered_sects, escape_rate, has_bahongchen
            FROM players
            ORDER BY cultivation DESC
        """).fetchall()
    
    players = []
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


if __name__ == '__main__':
    port = int(os.getenv('WEB_PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)
