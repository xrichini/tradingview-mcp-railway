# TradingView MCP Server for Railway

Deploy tradingview-mcp to Railway.app with **zero spin-down** and **$0 cost** for 3-6 months!

## 🚀 Why Railway instead of Render?

- ✅ **No spin-down** — always on (24/7, even on free tier)
- ✅ **Instant response** — no 30-second wake-up delay
- ✅ **Perfect for Claude.ai** — MCP responds fast enough
- ✅ **Free for 3-6 months** — $5 monthly credits automatically applied
- ✅ **Better DX** — real-time logs, instant deploys, better support

## ⚠️ Difference from Render

| Feature | Render | Railway |
|---------|--------|---------|
| Spin-down | ❌ After 15 min | ✅ Never |
| Wake time | ~30 sec | <200 ms |
| Claude.ai compatibility | ❌ Timeout issues | ✅ Works perfectly |
| Cost (free tier) | $0 forever | $0 first 3-6 months, $5/mo after |

## 📋 Files inside

- `Procfile` — tells Railway how to start the server
- `server.py` — wrapper that starts tradingview-mcp
- `requirements.txt` — Python dependencies (just uv)
- `build.sh` — build script (installs uv)
- `railway.json` — optional config file
- `.gitignore` — git ignore rules

## 🚀 Deploy to Railway (3 steps)

### Step 1: Push to GitHub

```bash
git init
git add .
git commit -m "Deploy tradingview-mcp to Railway"
git remote add origin https://github.com/YOUR-USERNAME/tradingview-mcp-railway
git push -u origin main
```

### Step 2: Create Railway Project

1. Go to https://railway.app
2. Click **New Project**
3. Select **Deploy from GitHub repo**
4. Select your `tradingview-mcp-railway` repo
5. Railway auto-detects the Procfile
6. Click **Deploy** → wait 2-3 minutes

### Step 3: Add to Claude.ai

1. Go to https://claude.ai
2. Settings → MCPs
3. Add new MCP:
   ```json
   {
     "name": "tradingview-mcp",
     "url": "https://tradingview-mcp-xxx.railway.app"
   }
   ```
   (Replace `xxx` with your Railway project ID from the dashboard)
4. Test in chat

## 🔗 Get Your URL

In Railway dashboard:
- Select your service
- Go to **Deployments**
- Look for the URL like `https://tradingview-mcp-xxx.railway.app`
- This is what you paste into Claude.ai settings

## 📊 Available Tools

Once connected, you have 27 tools:

- `market_snapshot` — Global market overview
- `top_gainers` / `top_losers` — Market screening
- `multi_agent_analysis` — Tech + Sentiment + Risk
- `combined_analysis` — TradingView + Reddit + News
- `coin_analysis` — Deep asset analysis
- And 22 more...

## 💡 Pro Tips

- **Real-time logs**: Railway dashboard → Deployments → Logs tab
- **Auto-redeploy**: Push to GitHub, Railway deploys automatically in ~30 sec
- **Free tier details**: $5 monthly credits, never expires (keep deploying, it keeps working)
- **After free credits**: Choose: keep paying $5/mo, switch to GitHub Actions, or self-host

## ❓ Troubleshooting

### "Can't connect to the URL"
1. Wait 2 minutes after deploy
2. Check Railway dashboard → Deployments for build/deploy errors
3. View logs: Deployments → Logs tab

### "MCP not responding in Claude.ai"
1. Verify the URL is correct (no typos)
2. Check Railway logs for errors
3. Test the URL directly in a browser: https://your-url.railway.app
   Should show MCP connection info

### "Want to see debug info"
Railway dashboard → Service → Logs → filter by "error"

## 🎯 Next Steps

1. Test your MCP in Claude.ai chat
2. Build your daily market-regime workflow
3. Consider GitHub Actions for automated daily reports
4. Integrate with finviz-mcp v3 (breadth indicators)

## 📚 Links

- Railway docs: https://docs.railway.app
- Procfile format: https://devcenter.heroku.com/articles/procfile
- MCP protocol: https://modelcontextprotocol.io
- Railway pricing: https://railway.app/pricing
