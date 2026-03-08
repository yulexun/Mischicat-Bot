#!/bin/bash

# Load environment variables
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
fi

# Default values
: ${WEB_PORT:=5000}
: ${FLASK_DEBUG:=False}
: ${DB_PATH:=game.db}

echo "Starting Mischicat Bot Web Dashboard..."
echo "Port: ${WEB_PORT}"
echo "Debug Mode: ${FLASK_DEBUG}"
echo "Database: ${DB_PATH}"
echo ""
echo "Dashboard will be available at: http://localhost:${WEB_PORT}"
echo "Press Ctrl+C to stop"
echo ""

# Run the web server
python3 web_server.py
