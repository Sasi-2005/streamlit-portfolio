import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ─────────────────────────────────────────────
#  EMAIL CONFIG — fill these in
# ─────────────────────────────────────────────
SMTP_HOST     = "smtp.gmail.com"
SMTP_PORT     = 587
YOUR_EMAIL    = "your@gmail.com"       # your Gmail address
YOUR_PASSWORD = "xxxx xxxx xxxx xxxx"  # Gmail App Password (not your login password)
                                        # Get it at: myaccount.google.com > Security > App Passwords

def send_email(sender_name, sender_email, message):
    try:
        msg = MIMEMultipart()
        msg["From"]    = YOUR_EMAIL
        msg["To"]      = YOUR_EMAIL
        msg["Subject"] = f"Portfolio Contact from {sender_name}"
        body = f"""
New message from your portfolio contact form:

Name:    {sender_name}
Email:   {sender_email}
Message: {message}
"""
        msg.attach(MIMEText(body, "plain"))
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(YOUR_EMAIL, YOUR_PASSWORD)
            server.sendmail(YOUR_EMAIL, YOUR_EMAIL, msg.as_string())
        return True
    except Exception as e:
        return str(e)


st.set_page_config(
    page_title="My Portfolio",
    page_icon="👤",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

:root {
    --accent: #5b8dee;
    --accent-light: #e8f0fe;
    --bg: #f4f6fb;
    --card-bg: #ffffff;
    --border: #e2e8f0;
    --text: #1e293b;
    --muted: #64748b;
    --header-bg: #0f172a;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background: var(--bg);
    color: var(--text);
}
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }
.block-container { padding: 0 2rem 5rem 2rem; max-width: 960px; margin: auto; }

/* ── HEADER ── */
.header {
    background: var(--header-bg);
    border-radius: 0 0 20px 20px;
    padding: 3rem 2.5rem 2.5rem 2.5rem;
    margin-bottom: 2.5rem;
    border-top: 4px solid var(--accent);
    position: relative;
    overflow: hidden;
}
.header::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 220px; height: 220px;
    border-radius: 50%;
    background: rgba(91,141,238,0.08);
}
.header::after {
    content: '';
    position: absolute;
    bottom: -40px; left: -40px;
    width: 160px; height: 160px;
    border-radius: 50%;
    background: rgba(91,141,238,0.05);
}
.header-top {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1.5rem;
    margin-bottom: 1.2rem;
}
.header-photo img {
    width: 90px; height: 90px;
    border-radius: 50%;
    object-fit: cover;
    border: 3px solid var(--accent);
    box-shadow: 0 0 0 5px rgba(91,141,238,0.15);
}
.photo-circle {
    width: 90px; height: 90px;
    border-radius: 50%;
    background: rgba(91,141,238,0.12);
    display: flex; align-items: center; justify-content: center;
    font-size: 2.2rem;
    border: 3px solid var(--accent);
    box-shadow: 0 0 0 5px rgba(91,141,238,0.15);
    flex-shrink: 0;
}
.header-name-wrap { display: flex; flex-direction: column; gap: 0.3rem; text-align: left; }
.header-name {
    font-size: 2.4rem;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: -0.02em;
    line-height: 1.1;
}
.header-role {
    font-size: 0.95rem;
    color: var(--accent);
    font-weight: 500;
    letter-spacing: 0.01em;
}
.header-desc {
    font-size: 0.9rem;
    color: rgba(255,255,255,0.55);
    line-height: 1.75;
    font-weight: 300;
    max-width: 560px;
    text-align: center;
    margin: 0 auto;
}

/* ── DIVIDER ── */
.divider { display: none; }

/* ── SECTION HEADING ── */
.section-heading {
    font-size: 0.7rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    color: var(--accent);
    margin-bottom: 0.4rem;
}
.section-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: #ffffff;
    margin: 0 0 1.8rem 0;
    letter-spacing: -0.01em;
}

/* ── PROJECT BOXES ── */
.proj-box {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.3rem 1.2rem 1.1rem 1.2rem;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    margin-bottom: 1rem;
    transition: box-shadow 0.2s, transform 0.2s, border-color 0.2s;
    position: relative;
    overflow: hidden;
}
.proj-box::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, var(--accent), #93c5fd);
    opacity: 0;
    transition: opacity 0.2s;
}
.proj-box:hover {
    box-shadow: 0 8px 30px rgba(91,141,238,0.12);
    transform: translateY(-2px);
    border-color: #c7d9fc;
}
.proj-box:hover::before { opacity: 1; }
.proj-title {
    font-size: 0.95rem;
    font-weight: 600;
    color: var(--text);
    line-height: 1.3;
}
.proj-desc {
    font-size: 0.8rem;
    color: var(--muted);
    line-height: 1.65;
    font-weight: 400;
    flex: 1;
}
.proj-tags { display: flex; flex-wrap: wrap; gap: 0.3rem; margin-top: 0.3rem; }
.proj-tag {
    font-size: 0.67rem;
    background: var(--accent-light);
    color: var(--accent);
    padding: 0.18rem 0.55rem;
    border-radius: 20px;
    font-weight: 500;
}
.proj-link {
    font-size: 0.75rem;
    color: var(--accent);
    font-weight: 500;
    text-decoration: none;
    margin-top: 0.4rem;
    display: inline-flex;
    align-items: center;
    gap: 0.2rem;
}
.proj-link:hover { text-decoration: underline; }

/* ── CONTACT ── */
.contact-block {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.8rem;
}
.contact-row { display: flex; flex-direction: column; gap: 0.9rem; }
.contact-line { display: flex; gap: 1rem; align-items: center; font-size: 0.9rem; }
.c-label {
    color: var(--muted);
    min-width: 80px;
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    font-weight: 500;
}
.c-val { color: var(--text); font-weight: 400; }

/* ── FORM ── */
.stTextInput label, .stTextArea label {
    font-size: 0.8rem !important;
    font-weight: 500 !important;
    color: var(--muted) !important;
}
.stTextInput input, .stTextArea textarea {
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    background: #f8faff !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.88rem !important;
    color: var(--text) !important;
    padding: 0.6rem 0.9rem !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 3px rgba(91,141,238,0.12) !important;
}
.stFormSubmitButton button {
    background: var(--accent) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    padding: 0.6rem 1.8rem !important;
    transition: background 0.2s !important;
}
.stFormSubmitButton button:hover { background: #4a7de0 !important; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  ✏️  EDIT YOUR INFO HERE
# ─────────────────────────────────────────────
NAME  = "Sasibhusana Behera"
ROLE  = "Quantitative Developer | Algorithmic Trading | Financial Modeling"
PHOTO = "sasi img latest.jpg"   # set to a file path like "photo.jpg" or a URL to show your photo

CONTACT = {
    "Email":    "contact.sasibhusana@gmail.com",
    "Location": "Bangalore, India",
    "GitHub":   "github.com/Sasi-2005",
    "LinkedIn": "linkedin.com/in/sasibhusana-b-b30956250/",
}

PROJECTS = [
    # Row 1
    {"title": "NeuralChat",     "desc": "Real-time AI chat platform with multi-model routing and streaming. Serves 10k+ monthly users.",                     "tags": ["Python", "FastAPI", "React"],     "link": "https://github.com"},
    {"title": "DataVault",      "desc": "Analytics pipeline on dbt + Airflow with a Streamlit BI dashboard. Cut reporting time by 60%.",                    "tags": ["Streamlit", "dbt", "PostgreSQL"],  "link": "https://github.com"},
    {"title": "GridQL",         "desc": "Visual SQL query builder that compiles drag-and-drop blocks into optimised SQL with live previews.",                "tags": ["TypeScript", "React", "Node.js"],  "link": "https://github.com"},
    # Row 2
    {"title": "Snapdeploy",     "desc": "One-command Kubernetes deployment CLI with secret management and rollback. 500+ GitHub stars.",                     "tags": ["Go", "Kubernetes", "Docker"],      "link": "https://github.com"},
    {"title": "StyleMorph",     "desc": "Neural style-transfer web app using a fine-tuned diffusion model. Upload a photo, get gallery-quality art.",        "tags": ["PyTorch", "FastAPI", "Next.js"],   "link": "https://github.com"},
    {"title": "OpenMetrics",    "desc": "Lightweight self-hosted monitoring tool with Prometheus-compatible scraping and dashboard alerts.",                  "tags": ["Rust", "TimescaleDB", "Svelte"],   "link": "https://github.com"},
    # Row 3
    {"title": "TaskFlow",       "desc": "Drag-and-drop project management tool with real-time collaboration, comments, and Slack integration.",              "tags": ["React", "Socket.io", "MongoDB"],   "link": "https://github.com"},
    {"title": "PriceTracker",   "desc": "E-commerce price monitor that scrapes 50+ sites and sends alerts when prices drop below your target.",             "tags": ["Python", "BeautifulSoup", "Redis"], "link": "https://github.com"},
    {"title": "DocuMind",       "desc": "AI-powered document Q&A tool. Upload PDFs and ask questions; powered by RAG with GPT-4 and Pinecone.",             "tags": ["Python", "LangChain", "Pinecone"], "link": "https://github.com"},
    # Row 4
    {"title": "SwiftCart",      "desc": "Headless e-commerce storefront with sub-100ms page loads, Stripe checkout, and inventory management.",              "tags": ["Next.js", "Stripe", "Sanity"],     "link": "https://github.com"},
    {"title": "LogLens",        "desc": "Structured log analysis tool with regex-based filtering, anomaly detection, and exportable reports.",               "tags": ["Python", "Elasticsearch", "Vue"],  "link": "https://github.com"},
    {"title": "CryptoBot",      "desc": "Automated trading bot with backtesting engine, live signals, and a clean Streamlit dashboard.",                     "tags": ["Python", "CCXT", "Streamlit"],     "link": "https://github.com"},
    # Row 5
    {"title": "AuthKit",        "desc": "Drop-in authentication library for FastAPI with JWT, OAuth2, RBAC, and rate limiting out of the box.",              "tags": ["Python", "FastAPI", "JWT"],        "link": "https://github.com"},
    {"title": "MapStudio",      "desc": "Geospatial data visualisation tool for plotting, filtering, and exporting large datasets on interactive maps.",     "tags": ["Python", "Folium", "GeoPandas"],   "link": "https://github.com"},
    {"title": "FormCraft",      "desc": "No-code form builder with conditional logic, file uploads, webhooks, and a shareable public link.",                 "tags": ["React", "Node.js", "MongoDB"],     "link": "https://github.com"},
]


# ─────────────────────────────────────────────
#  HEADER — Name & Role
# ─────────────────────────────────────────────
BIO_SHORT = "Aspiring quantitative developer with a strong interest in financial markets, data analysis, and quantitative modeling. I build data-driven financial models and trading strategies using tools such as Python, while applying concepts from statistics and Machine Learning to better understand and analyze market behavior."

# ── Header: photo left, name right, desc below ──
import base64, os

def get_photo_html(photo_path):
    if not photo_path:
        return '<div class="photo-circle">👤</div>'
    if photo_path.startswith("http"):
        return f'<img src="{photo_path}">'
    if os.path.exists(photo_path):
        ext = photo_path.split(".")[-1]
        with open(photo_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        return f'<img src="data:image/{ext};base64,{b64}">'
    return '<div class="photo-circle">👤</div>'

photo_html = get_photo_html(PHOTO)

st.markdown(f"""
<div class="header">
  <div class="header-top">
    <div class="header-photo">{photo_html}</div>
    <div class="header-name-wrap">
      <div class="header-name">{NAME}</div>
      <div class="header-role">{ROLE}</div>
    </div>
  </div>
  <div class="header-desc">{BIO_SHORT}</div>
</div>
""", unsafe_allow_html=True)


st.markdown('<hr class="divider">', unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  PROJECTS
# ─────────────────────────────────────────────
st.markdown('<div class="section-heading">Work</div><div class="section-title">Projects</div>', unsafe_allow_html=True)

# Build rows of 3
rows = [PROJECTS[i:i+3] for i in range(0, len(PROJECTS), 3)]

for row in rows:
    cols = st.columns(3, gap="small")
    for col, proj in zip(cols, row):
        tags_html = "".join(f'<span class="proj-tag">{t}</span>' for t in proj["tags"])
        col.markdown(f"""
        <div class="proj-box">
          <div class="proj-title">{proj['title']}</div>
          <div class="proj-desc">{proj['desc']}</div>
          <div class="proj-tags">{tags_html}</div>
          <a class="proj-link" href="{proj['link']}" target="_blank">View project ↗</a>
        </div>
        """, unsafe_allow_html=True)


st.markdown('<hr class="divider">', unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  CONTACT
# ─────────────────────────────────────────────
st.markdown('<div class="section-heading">Get in touch</div><div class="section-title">Contact</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    rows_html = "".join(
        f'<div class="contact-line"><span class="c-label">{k}</span><span class="c-val">{v}</span></div>'
        for k, v in CONTACT.items()
    )
    st.markdown(f"""
    <div class="contact-block">
      <div class="contact-row">{rows_html}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    with st.form("contact_form", clear_on_submit=True):
        name_in  = st.text_input("Name",    placeholder="Your name")
        email_in = st.text_input("Email",   placeholder="your@email.com")
        msg_in   = st.text_area("Message",  placeholder="Say hello...", height=100)
        if st.form_submit_button("Send message"):
            if name_in and email_in and msg_in:
                result = send_email(name_in, email_in, msg_in)
                if result is True:
                    st.success("Message sent! I'll reply soon.")
                else:
                    st.error(f"Failed to send: {result}")
            else:

                st.warning("Please fill in all fields.")


