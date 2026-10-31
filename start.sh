#!/bin/bash
# Start script for Render deployment
# This script starts the mistake-finder package as a web service

set -e

echo "Starting mistake-finder..."

# Install the package
pip install . --quiet

# Verify installation
python -c "import mistake_finder; print('mistake-finder ready')"

# Start a simple HTTP server for health checks
exec python -c "
from http.server import HTTPServer, SimpleHTTPRequestHandler

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>mistake-finder</h1><p>Python CLI tool ready</p>')
    
    def log_message(self, format, *args):
        pass

HTTPServer(('0.0.0.0', 8080), Handler).serve_forever()
"
