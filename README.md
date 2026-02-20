# 🔮 AI Stock Market Sentiment Oracle

> **Claude-powered news & social media analyzer that predicts stock market sentiment and detects trend shifts before they happen.**

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32%2B-FF4B4B?style=flat-square&logo=streamlit)
![Anthropic](https://img.shields.io/badge/Claude-claude--opus--4--6-purple?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 📌 Overview

The **AI Sentiment Oracle** is a Streamlit web application that uses **Anthropic's Claude AI** to perform deep, Wall-Street-grade sentiment analysis on raw news articles and social media posts. It identifies crowd psychology, detects upcoming trend shifts, and produces actionable trade signals — all in seconds.

### What it does

- Accepts raw **news headlines / articles** and **social media posts** (tweets, Reddit, StockTwits, etc.)
- Sends them to Claude with a structured prompt designed by a quantitative finance expert
- Returns a rich JSON analysis rendered as an interactive dashboard
- Tracks multiple sessions of analysis in a **Signal History** tab

---

## ✨ Features

| Feature | Description |
|---|---|
| 🧠 **AI Sentiment Score** | -100 (extreme bearish) to +100 (extreme bullish) |
| 📈 **Trend Direction** | 7-level trend classification with confidence score |
| 🔄 **Trend Shift Probability** | Probability (0–100%) that sentiment will reverse |
| 😰 **Fear & Greed Index** | Derived from text signals, 0–100 |
| 👥 **Retail vs Institutional Sentiment** | Separate scores for each cohort |
| ⚡ **Contrarian Signal** | Strong Buy → Strong Sell fade signal |
| 🧠 **Crowd Psychology** | FOMO / Euphoria / Panic / Capitulation / etc. |
| 📰 **News vs Social Divergence** | Detects when media and social crowd disagree |
| 🎯 **Key Drivers** | Top 5 factors with impact and strength rating |
| ⚠️ **Risk Factors** | 3 key risks to the current thesis |
| 🚨 **Catalysts to Watch** | Upcoming events that could shift sentiment |
| 📝 **Expert Analysis** | 3–4 paragraph CNBC-style analyst commentary |
| 🏹 **Trade Signal** | LONG / SHORT / FLAT with conviction level |

---

## 🚀 Quick Start

### 1. Clone or download the project

```bash
git clone https://github.com/yourname/ai-sentiment-oracle.git
cd ai-sentiment-oracle
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv

# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Get your Anthropic API Key

1. Go to [https://console.anthropic.com](https://console.anthropic.com)
2. Sign up or log in
3. Navigate to **API Keys** and create a new key
4. Copy the key (starts with `sk-ant-...`)

### 5. Run the app

```bash
streamlit run ai_sentiment_analyzer.py
```

Your browser will open automatically at `http://localhost:8501`

---

## 🖥️ How to Use

### Step 1 — Enter your API Key
In the **left sidebar**, paste your Anthropic API key into the **API Key** field. It is used only for the current session and never stored.

### Step 2 — Configure your analysis
- **Target Ticker / Asset** — e.g. `NVDA`, `BTC`, `SPX`, or leave blank for overall market
- **Prediction Timeframe** — choose from 24 hours to 1 month
- **Analysis Mode** — Standard, Deep Dive, or Contrarian Focus

### Step 3 — Paste your data
Go to the **📥 INPUT DATA** tab:
- **Left panel** — paste news headlines, earnings reports, macro data, analyst notes
- **Right panel** — paste tweets, Reddit posts, Discord messages, StockTwits

> 💡 Sample data is pre-loaded so you can try it immediately without any input.

### Step 4 — Run analysis
Click **🔮 RUN AI SENTIMENT ANALYSIS**. Claude will process the content and return results in 10–20 seconds.

### Step 5 — Review results
Switch to the **📊 ANALYSIS RESULTS** tab to see:
- Sentiment score, trend direction, and shift probability
- Fear & Greed index, retail vs institutional sentiment
- Key drivers, risk factors, and catalysts
- Expert analyst commentary
- Trade signal with conviction rating

---

## 📂 Project Structure

```
ai-sentiment-oracle/
│
├── ai_sentiment_analyzer.py   # Main Streamlit application
├── requirements.txt           # Python dependencies
├── README.md                  # This file
│
└── (optional future additions)
    ├── utils/
    │   ├── scraper.py         # Auto-fetch news from RSS feeds
    │   └── twitter_api.py     # Pull live tweets via Twitter API v2
    └── history/
        └── signals.json       # Persisted signal history
```

---

## 🧩 How the AI Analysis Works

The app sends a carefully engineered **system prompt + user prompt** to `claude-opus-4-6`:

```
System: You are an elite quantitative analyst with 20+ years on Wall Street...

User:  TARGET: {ticker}
       TIMEFRAME: {timeframe}

       === NEWS ===
       {pasted news}

       === SOCIAL MEDIA ===
       {pasted social posts}

       Return structured JSON with sentiment score, trend, signals...
```

Claude returns a structured **JSON object** with 15+ fields that are parsed and rendered into the dashboard.

---

## ⚙️ Configuration Options

| Setting | Options | Default |
|---|---|---|
| Timeframe | 24h / 3d / 1w / 2w / 1mo | Next Week |
| Analysis Mode | Standard / Deep Dive / Contrarian | Standard |
| Target Asset | Any ticker or blank for SPX | (blank) |
| Auto-refresh | On / Off | Off |

---

## 🔒 Privacy & Security

- Your **API key is never stored** — it lives only in the Streamlit session state
- No data is sent anywhere except directly to the **Anthropic API**
- No telemetry or logging is performed by this app

---

## ⚠️ Disclaimer

> This tool is for **educational and research purposes only**. It does **not** constitute financial advice. Always do your own research before making investment decisions. Past sentiment signals do not guarantee future market performance. The developers are not responsible for any financial losses.

---

## 🛠️ Troubleshooting

**`ModuleNotFoundError: No module named 'anthropic'`**
```bash
pip install -r requirements.txt
```

**`AuthenticationError` from Anthropic**
- Double-check your API key in the sidebar
- Make sure it starts with `sk-ant-`
- Verify you have credits at [console.anthropic.com](https://console.anthropic.com)

**`JSONDecodeError` on analysis**
- This can rarely happen if Claude's response is malformed — just click **Run Analysis** again

**App is slow to load**
- First run may take ~20 seconds as Claude processes the text
- Reduce the amount of text input for faster results

**Port already in use**
```bash
streamlit run ai_sentiment_analyzer.py --server.port 8502
```

---

## 🔮 Roadmap

- [ ] Auto-fetch news via RSS feeds (Reuters, Bloomberg, CNBC)
- [ ] Twitter / X API live tweet ingestion
- [ ] Reddit API integration (r/wallstreetbets, r/investing)
- [ ] Historical signal backtesting
- [ ] Export analysis to PDF report
- [ ] Email/Slack alert when shift probability exceeds threshold
- [ ] Multi-ticker comparison dashboard
- [ ] Portfolio-level sentiment aggregation

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## 🙏 Credits

Built with [Streamlit](https://streamlit.io) · Powered by [Anthropic Claude](https://anthropic.com) · Designed for traders, analysts, and fintech builders.
