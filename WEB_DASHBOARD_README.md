# Web Dashboard

This directory contains the web dashboard for viewing all player information from the Mischicat Bot cultivation game.

## Features

- **Real-time Player Statistics**: View all players' cultivation progress, realm, spirit stones, and more
- **Search & Filter**: Search by name, realm, sect, or city. Filter by player status (alive/dead)
- **Sortable Columns**: Click on column headers to sort players by different attributes
- **Pagination**: Browse through large player lists with easy pagination
- **Auto-refresh**: Dashboard automatically refreshes every 30 seconds
- **Overall Statistics**: View total players, alive/dead counts, and total spirit stones in circulation

## Installation

The Flask dependency has already been added to `requirements.txt`. To install:

```bash
pip install -r requirements.txt
```

## Running the Dashboard

### Option 1: Direct Python Execution

```bash
python web_server.py
```

The dashboard will be available at `http://localhost:5000`

### Option 2: Using Docker Compose

The web dashboard is configured in `docker-compose.yml`. To run both the bot and dashboard:

```bash
docker-compose up -d
```

The dashboard will be available at `http://localhost:5000` (or whatever port you configured in `.env`)

To run only the dashboard:

```bash
docker-compose up -d web-dashboard
```

## Configuration

Add the following environment variables to your `.env` file:

```env
WEB_PORT=5000          # Port for the web server (default: 5000)
FLASK_DEBUG=False      # Enable Flask debug mode (default: False)
DB_PATH=game.db        # Path to SQLite database (shared with bot)
```

## API Endpoints

The dashboard provides the following API endpoints:

### GET `/api/players`

Returns all player data with cultivation information.

**Response:**
```json
{
  "success": true,
  "total": 42,
  "players": [
    {
      "discord_id": "123456789",
      "name": "张三",
      "realm": "炼气期三层",
      "cultivation": 150,
      "spirit_stones": 1200,
      ...
    }
  ]
}
```

### GET `/api/stats`

Returns overall game statistics.

**Response:**
```json
{
  "success": true,
  "stats": {
    "total_players": 42,
    "alive_players": 38,
    "dead_players": 4,
    "total_spirit_stones": 125000,
    "sects": [...],
    "realms": [...],
    "top_cultivators": [...]
  }
}
```

## Dashboard Features

### Statistics Cards

- **总玩家数**: Total number of registered players
- **健在玩家**: Number of living players
- **已坐化**: Number of deceased players
- **灵石总量**: Total spirit stones in circulation (among living players)

### Player Table

The table displays the following information for each player:

- Name (姓名)
- Gender (性别)
- Realm (境界)
- Cultivation Points (修为)
- Spirit Stones (灵石)
- Lifespan (寿元)
- Spirit Root (灵根)
- Sect (宗门)
- Current City (所在城市)
- Status (状态)
- Last Active (最后活跃)

### Controls

- **Search Box**: Filter players by name, realm, sect, or city
- **Filter Buttons**: 
  - 全部 (All): Show all players
  - 健在 (Alive): Show only living players
  - 已坐化 (Dead): Show only deceased players
- **Refresh Button**: Manually refresh the data

### Sorting

Click on column headers to sort:
- Name, Realm, Cultivation, Spirit Stones, Lifespan, Last Active

Click again to toggle between ascending and descending order.

## Screenshots

![Dashboard Overview](screenshots/dashboard.png)

## Troubleshooting

### Port Already in Use

If port 5000 is already in use, change the `WEB_PORT` in your `.env` file:

```env
WEB_PORT=8080
```

### Database Connection Issues

Make sure the `DB_PATH` environment variable points to the same database file used by the bot.

### Permission Issues with Docker

If you encounter permission issues with the SQLite database in Docker, ensure the volume has proper permissions:

```bash
docker-compose down
sudo chown -R 1000:1000 sqlite-data/
docker-compose up -d
```

## Development

To enable debug mode for development:

```env
FLASK_DEBUG=True
```

This will enable auto-reload when you make changes to the code.

## Security Considerations

- The dashboard does not include authentication by default
- For production use, consider adding authentication middleware
- Restrict access using firewall rules or reverse proxy (nginx, Apache)
- Use HTTPS in production environments

## Future Enhancements

Potential features to add:

- User authentication and authorization
- Real-time updates using WebSockets
- Player detail pages with full history
- Charts and graphs for cultivation progress
- Export data to CSV/JSON
- Admin panel for player management
- Sect rankings and leaderboards
- Battle history and statistics
