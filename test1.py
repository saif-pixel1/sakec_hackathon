import streamlit as st
import random
import datetime
import time

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Market Sentiment Tracker",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Bebas+Neue&family=DM+Sans:wght@300;400;600&display=swap');

:root {
    --bg: #070b14;
    --surface: #0d1526;
    --surface2: #111d35;
    --accent-green: #00ff9d;
    --accent-red: #ff3b5c;
    --accent-yellow: #ffd166;
    --accent-blue: #4cc9f0;
    --text: #c8d8f0;
    --muted: #4a607a;
    --border: #1a2e4a;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--bg);
    color: var(--text);
}

.stApp {
    background: radial-gradient(ellipse at top left, #0d1a2e 0%, #070b14 60%);
}

/* Hide streamlit branding */
#MainMenu, footer, header { visibility: hidden; }

/* Sidebar */
section[data-testid="stSidebar"] {
    background: var(--surface) !important;
    border-right: 1px solid var(--border);
}

/* Title */
.main-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 3.2rem;
    letter-spacing: 0.12em;
    color: var(--accent-blue);
    text-shadow: 0 0 30px rgba(76,201,240,0.4);
    line-height: 1;
    margin-bottom: 0;
}
.sub-title {
    font-family: 'Share Tech Mono', monospace;
    color: var(--muted);
    font-size: 0.8rem;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    margin-bottom: 1.5rem;
}

/* Metric Cards */
.metric-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 1.2rem 1.4rem;
    position: relative;
    overflow: hidden;
}
.metric-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
}
.metric-card.green::before { background: var(--accent-green); box-shadow: 0 0 12px var(--accent-green); }
.metric-card.red::before { background: var(--accent-red); box-shadow: 0 0 12px var(--accent-red); }
.metric-card.blue::before { background: var(--accent-blue); box-shadow: 0 0 12px var(--accent-blue); }
.metric-card.yellow::before { background: var(--accent-yellow); box-shadow: 0 0 12px var(--accent-yellow); }

.metric-label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.2em;
    color: var(--muted);
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}
.metric-value {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2.4rem;
    line-height: 1;
}
.metric-value.green { color: var(--accent-green); }
.metric-value.red { color: var(--accent-red); }
.metric-value.blue { color: var(--accent-blue); }
.metric-value.yellow { color: var(--accent-yellow); }

.metric-delta {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.75rem;
    color: var(--muted);
    margin-top: 0.2rem;
}

/* Ticker row */
.ticker-bar {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 0.6rem 1rem;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.85rem;
    margin-bottom: 1rem;
}

/* News card */
.news-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-left: 3px solid;
    border-radius: 6px;
    padding: 0.9rem 1rem;
    margin-bottom: 0.6rem;
}
.news-card.bullish { border-left-color: var(--accent-green); }
.news-card.bearish { border-left-color: var(--accent-red); }
.news-card.neutral { border-left-color: var(--muted); }

.news-headline {
    font-size: 0.9rem;
    font-weight: 600;
    color: var(--text);
    margin-bottom: 0.3rem;
}
.news-meta {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.7rem;
    color: var(--muted);
}
.sentiment-badge {
    display: inline-block;
    padding: 0.15rem 0.5rem;
    border-radius: 3px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.65rem;
    font-weight: bold;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}
.badge-bullish { background: rgba(0,255,157,0.15); color: var(--accent-green); }
.badge-bearish { background: rgba(255,59,92,0.15); color: var(--accent-red); }
.badge-neutral { background: rgba(74,96,122,0.15); color: var(--muted); }

/* Fear/Greed gauge label */
.gauge-label {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.4rem;
    letter-spacing: 0.1em;
    text-align: center;
}

/* Section header */
.section-header {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.3em;
    color: var(--muted);
    text-transform: uppercase;
    border-bottom: 1px solid var(--border);
    padding-bottom: 0.4rem;
    margin-bottom: 0.8rem;
}

/* Buttons */
.stButton > button {
    background: transparent !important;
    border: 1px solid var(--accent-blue) !important;
    color: var(--accent-blue) !important;
    font-family: 'Share Tech Mono', monospace !important;
    letter-spacing: 0.1em !important;
    border-radius: 4px !important;
    transition: all 0.2s !important;
}
.stButton > button:hover {
    background: rgba(76,201,240,0.1) !important;
    box-shadow: 0 0 15px rgba(76,201,240,0.2) !important;
}

/* Selectbox, multiselect, slider */
.stSelectbox > div, .stMultiSelect > div {
    background: var(--surface2) !important;
    border-color: var(--border) !important;
    color: var(--text) !important;
}

/* Progress bar */
.stProgress > div > div > div {
    background: linear-gradient(90deg, var(--accent-green), var(--accent-blue)) !important;
}
</style>
""", unsafe_allow_html=True)

# ─── Simulated Data ──────────────────────────────────────────────────────────
STOCKS = {
    "AAPL": {"name": "Apple Inc.", "price": 189.45, "change": 1.23, "sector": "Technology"},
    "MSFT": {"name": "Microsoft Corp.", "price": 415.20, "change": -0.87, "sector": "Technology"},
    "NVDA": {"name": "NVIDIA Corp.", "price": 875.60, "change": 3.45, "sector": "Technology"},
    "TSLA": {"name": "Tesla Inc.", "price": 248.30, "change": -2.10, "sector": "Automotive"},
    "AMZN": {"name": "Amazon.com Inc.", "price": 192.80, "change": 0.95, "sector": "E-Commerce"},
    "GOOGL": {"name": "Alphabet Inc.", "price": 165.70, "change": 1.10, "sector": "Technology"},
    "META":  {"name": "Meta Platforms", "price": 513.40, "change": 2.30, "sector": "Social Media"},
    "JPM":   {"name": "JPMorgan Chase", "price": 198.60, "change": -0.45, "sector": "Finance"},
    "BTC-USD": {"name": "Bitcoin", "price": 64800.0, "change": 2.80, "sector": "Crypto"},
    "ETH-USD": {"name": "Ethereum", "price": 3420.0, "change": -1.20, "sector": "Crypto"},
}

HEADLINES = [
    ("Fed signals potential rate cuts in Q2 amid cooling inflation data", "bullish", "Reuters"),
    ("NVDA beats earnings expectations by 18%, raises full-year guidance", "bullish", "Bloomberg"),
    ("Treasury yields spike to 4.8%, rattling equity markets", "bearish", "WSJ"),
    ("Apple announces $110B buyback program, largest in company history", "bullish", "CNBC"),
    ("Oil prices surge 4% on Middle East supply concerns", "bearish", "Reuters"),
    ("Meta Platforms reports record ad revenue growth of 27% YoY", "bullish", "Bloomberg"),
    ("China GDP growth misses estimates, global demand concerns rise", "bearish", "FT"),
    ("JPMorgan downgrades Tesla on margin compression fears", "bearish", "Goldman Sachs"),
    ("Bitcoin ETF sees record inflows of $1.2B in single day", "bullish", "CoinDesk"),
    ("S&P 500 P/E ratio at 22x — analysts warn of stretched valuations", "neutral", "Barron's"),
    ("Amazon Web Services growth accelerates to 17% — cloud demand robust", "bullish", "CNBC"),
    ("EU imposes new AI regulation framework — tech stocks flat", "neutral", "Euronews"),
]

SECTORS = ["Technology", "Finance", "Energy", "Healthcare", "Consumer", "Automotive", "Crypto", "E-Commerce", "Social Media"]

def get_sentiment_label(score):
    if score < 25: return "EXTREME FEAR", "red"
    elif score < 40: return "FEAR", "red"
    elif score < 55: return "NEUTRAL", "yellow"
    elif score < 75: return "GREED", "green"
    else: return "EXTREME GREED", "green"

def get_market_color(change):
    return "green" if change >= 0 else "red"

def sentiment_emoji(s):
    return {"bullish": "▲", "bearish": "▼", "neutral": "◆"}[s]

# ─── Sidebar ─────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="section-header">⚙ CONTROLS</div>', unsafe_allow_html=True)

    selected_stocks = st.multiselect(
        "Watchlist",
        options=list(STOCKS.keys()),
        default=["AAPL", "NVDA", "TSLA", "BTC-USD"],
    )

    st.markdown('<div class="section-header">FILTERS</div>', unsafe_allow_html=True)
    sentiment_filter = st.selectbox("News Sentiment", ["All", "Bullish", "Bearish", "Neutral"])
    sector_filter = st.multiselect("Sectors", SECTORS, default=SECTORS[:4])

    st.markdown('<div class="section-header">SIMULATION</div>', unsafe_allow_html=True)
    volatility = st.slider("Market Volatility", 0.1, 3.0, 1.0, step=0.1)
    auto_refresh = st.checkbox("Auto-Refresh (5s)", value=False)

    st.markdown('<div class="section-header">INFO</div>', unsafe_allow_html=True)
    st.markdown(f'<span style="font-family:Share Tech Mono,monospace;font-size:0.7rem;color:#4a607a;">'
                f'LAST UPDATE<br>{datetime.datetime.now().strftime("%H:%M:%S — %d %b %Y")}</span>',
                unsafe_allow_html=True)

# ─── Auto-refresh ────────────────────────────────────────────────────────────
if auto_refresh:
    time.sleep(5)
    st.rerun()

# ─── Header ──────────────────────────────────────────────────────────────────
col_title, col_refresh = st.columns([5, 1])
with col_title:
    st.markdown('<div class="main-title">MARKET SENTIMENT</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">📡 Real-Time Intelligence Dashboard</div>', unsafe_allow_html=True)
with col_refresh:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("↻ REFRESH"):
        st.rerun()

# ─── Simulated live prices with noise ────────────────────────────────────────
def noisy(val, vol=1.0):
    return val * (1 + random.gauss(0, 0.002 * vol))

live_stocks = {k: {**v, "price": noisy(v["price"], volatility),
                    "change": v["change"] + random.gauss(0, 0.3 * volatility)}
               for k, v in STOCKS.items()}

# ─── Fear & Greed + Market Overview ──────────────────────────────────────────
fg_score = int(random.gauss(52, 8 * volatility))
fg_score = max(0, min(100, fg_score))
fg_label, fg_color = get_sentiment_label(fg_score)

bullish_pct = random.randint(48, 65)
bearish_pct = random.randint(20, 35)
neutral_pct = 100 - bullish_pct - bearish_pct
vix = round(random.gauss(18, 3 * volatility), 2)
put_call = round(random.gauss(0.92, 0.1 * volatility), 2)

m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown(f"""
    <div class="metric-card {fg_color}">
        <div class="metric-label">Fear & Greed Index</div>
        <div class="metric-value {fg_color}">{fg_score}</div>
        <div class="gauge-label" style="color:{'#00ff9d' if fg_color=='green' else '#ff3b5c' if fg_color=='red' else '#ffd166'}">{fg_label}</div>
    </div>""", unsafe_allow_html=True)

with m2:
    color2 = "green" if bullish_pct > 50 else "red"
    st.markdown(f"""
    <div class="metric-card {color2}">
        <div class="metric-label">Bullish Sentiment</div>
        <div class="metric-value {color2}">{bullish_pct}%</div>
        <div class="metric-delta">Bearish {bearish_pct}% · Neutral {neutral_pct}%</div>
    </div>""", unsafe_allow_html=True)

with m3:
    vix_color = "red" if vix > 20 else "green"
    st.markdown(f"""
    <div class="metric-card {vix_color}">
        <div class="metric-label">VIX Volatility Index</div>
        <div class="metric-value {vix_color}">{vix}</div>
        <div class="metric-delta">{'⚠ Elevated' if vix > 20 else '✓ Normal'} volatility regime</div>
    </div>""", unsafe_allow_html=True)

with m4:
    pc_color = "red" if put_call > 1.0 else "green"
    st.markdown(f"""
    <div class="metric-card blue">
        <div class="metric-label">Put/Call Ratio</div>
        <div class="metric-value blue">{put_call}</div>
        <div class="metric-delta">{'Bearish options flow' if put_call > 1.0 else 'Bullish options flow'}</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ─── Watchlist + Sector Heatmap ──────────────────────────────────────────────
col_watch, col_heat = st.columns([3, 2])

with col_watch:
    st.markdown('<div class="section-header">◈ WATCHLIST</div>', unsafe_allow_html=True)
    stocks_to_show = selected_stocks if selected_stocks else list(STOCKS.keys())[:5]
    for ticker in stocks_to_show:
        s = live_stocks[ticker]
        chg = s["change"]
        color = "green" if chg >= 0 else "red"
        arrow = "▲" if chg >= 0 else "▼"
        sign = "+" if chg >= 0 else ""
        # Sentiment score for each stock
        sent_score = random.randint(30, 85)
        sent_lbl, _ = get_sentiment_label(sent_score)
        st.markdown(f"""
        <div class="ticker-bar">
            <span style="font-size:1rem;color:var(--accent-blue);font-family:'Bebas Neue',sans-serif;letter-spacing:0.1em;">{ticker}</span>
            &nbsp;&nbsp;
            <span style="color:var(--text);font-size:0.85rem;">{s['name'][:20]}</span>
            &nbsp;&nbsp;&nbsp;
            <span style="color:var(--text);font-family:'Bebas Neue',sans-serif;font-size:1.1rem;">${s['price']:,.2f}</span>
            &nbsp;
            <span style="color:{'#00ff9d' if color=='green' else '#ff3b5c'};">{arrow} {sign}{chg:.2f}%</span>
            &nbsp;&nbsp;
            <span style="float:right;font-size:0.7rem;color:var(--muted);">Sentiment: {sent_score}/100</span>
        </div>""", unsafe_allow_html=True)

with col_heat:
    st.markdown('<div class="section-header">◈ SECTOR SENTIMENT</div>', unsafe_allow_html=True)
    sector_data = {
        "Technology": random.randint(55, 80),
        "Finance": random.randint(40, 65),
        "Energy": random.randint(35, 60),
        "Healthcare": random.randint(50, 75),
        "Consumer": random.randint(45, 70),
        "Crypto": random.randint(45, 85),
        "Automotive": random.randint(30, 60),
        "E-Commerce": random.randint(55, 75),
    }
    for sector, score in sector_data.items():
        lbl, color = get_sentiment_label(score)
        hex_color = "#00ff9d" if color == "green" else "#ff3b5c" if color == "red" else "#ffd166"
        st.markdown(f"""
        <div style="display:flex;align-items:center;margin-bottom:0.5rem;gap:0.8rem;">
            <span style="font-family:'Share Tech Mono',monospace;font-size:0.7rem;color:var(--muted);width:90px;flex-shrink:0;">{sector[:11].upper()}</span>
            <div style="flex:1;background:var(--surface2);border-radius:3px;height:6px;overflow:hidden;">
                <div style="width:{score}%;height:100%;background:{hex_color};border-radius:3px;box-shadow:0 0 6px {hex_color}55;"></div>
            </div>
            <span style="font-family:'Bebas Neue',sans-serif;font-size:0.9rem;color:{hex_color};width:30px;text-align:right;">{score}</span>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ─── Sentiment Trend + News ───────────────────────────────────────────────────
col_chart, col_news = st.columns([2, 3])

with col_chart:
    st.markdown('<div class="section-header">◈ SENTIMENT TREND (7D)</div>', unsafe_allow_html=True)
    import pandas as pd
    days = [(datetime.datetime.now() - datetime.timedelta(days=i)).strftime("%d %b") for i in range(6, -1, -1)]
    bull_trend = [random.randint(45, 70) for _ in days]
    bear_trend = [random.randint(20, 40) for _ in days]

    chart_df = pd.DataFrame({
        "Bullish %": bull_trend,
        "Bearish %": bear_trend,
    }, index=days)

    st.line_chart(chart_df, use_container_width=True, height=200,
                  color=["#00ff9d", "#ff3b5c"])

    # Social media buzz
    st.markdown('<div class="section-header" style="margin-top:1rem;">◈ SOCIAL BUZZ</div>', unsafe_allow_html=True)
    buzz = {
        "Twitter/X": random.randint(50000, 120000),
        "Reddit (WSB)": random.randint(8000, 25000),
        "StockTwits": random.randint(15000, 45000),
    }
    for platform, count in buzz.items():
        st.markdown(f"""
        <div style="display:flex;justify-content:space-between;padding:0.4rem 0;border-bottom:1px solid var(--border);">
            <span style="font-family:'Share Tech Mono',monospace;font-size:0.75rem;color:var(--muted);">{platform}</span>
            <span style="font-family:'Bebas Neue',sans-serif;color:var(--accent-blue);">{count:,} posts</span>
        </div>""", unsafe_allow_html=True)

with col_news:
    st.markdown('<div class="section-header">◈ SENTIMENT NEWS FEED</div>', unsafe_allow_html=True)
    filtered_news = HEADLINES
    if sentiment_filter != "All":
        filtered_news = [h for h in HEADLINES if h[1] == sentiment_filter.lower()]

    random.shuffle(filtered_news)
    for headline, sentiment, source in filtered_news[:8]:
        badge_class = f"badge-{sentiment}"
        card_class = f"news-card {sentiment}"
        emoji = sentiment_emoji(sentiment)
        st.markdown(f"""
        <div class="{card_class}">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:0.3rem;">
                <div class="news-headline">{headline}</div>
                <span class="sentiment-badge {badge_class}" style="margin-left:0.5rem;white-space:nowrap;">{emoji} {sentiment.upper()}</span>
            </div>
            <div class="news-meta">{source} · {random.randint(1, 59)}m ago</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ─── Bottom bar ──────────────────────────────────────────────────────────────
st.markdown(f"""
<div style="text-align:center;font-family:'Share Tech Mono',monospace;font-size:0.65rem;
color:#2a3d55;padding:1rem;border-top:1px solid #1a2e4a;margin-top:1rem;">
⚠ SIMULATED DATA FOR EDUCATIONAL PURPOSES ONLY · NOT FINANCIAL ADVICE ·
MARKET SENTIMENT TRACKER v1.0 · {datetime.datetime.now().strftime("%Y-%m-%d")}
</div>
""", unsafe_allow_html=True)