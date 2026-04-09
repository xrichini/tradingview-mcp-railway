#!/usr/bin/env python3
"""
TradingView MCP Server Wrapper for Railway deployment
Starts tradingview-mcp in streamable-http mode with proxy
"""

import os
import subprocess
import sys
import threading
import time
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
import httpx

app = FastAPI()

# Internal port for tradingview-mcp
INTERNAL_PORT = 8001
client = None

@app.get("/")
async def health():
    """Health check endpoint"""
    return JSONResponse({
        "status": "ok",
        "service": "tradingview-mcp",
        "version": "1.0",
        "message": "Add to Claude.ai: https://your-railway-url.railway.app"
    })

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy(path: str):
    """Proxy all other requests to the internal MCP server"""
    try:
        url = f"http://127.0.0.1:{INTERNAL_PORT}/{path}"
        async with httpx.AsyncClient() as client:
            response = await client.request(
                method="GET",
                url=url,
                follow_redirects=True
            )
            return JSONResponse(response.json(), status_code=response.status_code)
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

def start_mcp_server():
    """Start the tradingview-mcp server on internal port"""
    time.sleep(1)  # Wait for FastAPI to start
    
    host = "127.0.0.1"
    port = str(INTERNAL_PORT)
    
    print(f"\n🔄 Starting MCP server on {host}:{port}")
    
    cmd = [
        "uvx",
        "--from", "tradingview-mcp-server",
        "tradingview-mcp",
        "streamable-http",
        "--host", host,
        "--port", port
    ]
    
    try:
        subprocess.run(cmd, check=False)
    except Exception as e:
        print(f"❌ Error starting MCP: {e}")

def main():
    port = int(os.getenv("PORT", "8000"))
    host = os.getenv("HOST", "0.0.0.0")
    
    print(f"🚀 Starting TradingView MCP Server on {host}:{port}")
    print("=" * 70)
    
    # Start MCP server in background thread
    mcp_thread = threading.Thread(target=start_mcp_server, daemon=True)
    mcp_thread.start()
    
    # Start FastAPI proxy server
    uvicorn.run(app, host=host, port=port, log_level="info")

if __name__ == "__main__":
    main()
