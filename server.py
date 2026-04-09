#!/usr/bin/env python3
"""
TradingView MCP Server Wrapper for Railway deployment
Starts tradingview-mcp in streamable-http mode
"""

import os
import subprocess
import sys

def main():
    # Get port from environment or default to 8000
    # Railway sets $PORT automatically
    port = os.getenv("PORT", "8000")
    host = os.getenv("HOST", "0.0.0.0")
    
    print(f"🚀 Starting TradingView MCP Server on {host}:{port}")
    print("=" * 70)
    
    # Start tradingview-mcp in streamable-http mode
    cmd = [
        "uvx",
        "--from", "tradingview-mcp-server",
        "tradingview-mcp",
        "streamable-http",
        "--host", host,
        "--port", port
    ]
    
    print(f"Command: {' '.join(cmd)}")
    print("=" * 70)
    
    # Run the server
    try:
        proc = subprocess.run(cmd, check=False)
        sys.exit(proc.returncode)
    except KeyboardInterrupt:
        print("\n✓ Server stopped")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
