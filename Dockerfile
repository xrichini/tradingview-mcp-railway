# TradingView MCP Server for Railway
FROM python:3.11-slim

WORKDIR /app

# Install uv package manager
RUN pip install --no-cache-dir uv==0.11.2

# Copy application files
COPY server.py .
COPY requirements.txt .

# Set environment variables
ENV PORT=8000
ENV HOST=0.0.0.0

# Exposed port for Railway
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD python -c "import socket; socket.create_connection(('127.0.0.1', 8000), timeout=2)"

# Start the server
CMD ["python", "server.py"]
