import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="🌍 EcoEngineer - Core Concepts",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Green Theme Styling ---
st.markdown("""
<style>
    body { background-color: #f4faf4; font-family: "Segoe UI", Arial, sans-serif; }
    .header-container {
        background: linear-gradient(90deg, #2e7d32, #66bb6a);
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.15);
        text-align: center;
        margin-bottom: 1.5rem;
        color: white;
    }
    .header-container h1 { font-weight: 800; font-size: 2.3rem; margin:0; }
    .header-container p { margin:0.4rem 0 0 0; opacity:0.95; font-size: 1.1rem; }
    .system-card {
        background: #ffffff;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        text-align: center;
        border: 1px solid #c8e6c9;
        transition: all 0.25s ease;
    }
    .system-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.12);
        border-color: #81c784;
    }
    .system-card h3 { margin-bottom: 0.6rem; color:#2e7d32; }
    .stButton>button {
        width: 100%; border-radius: 8px;
        background-color: #388e3c; color: #fff;
        font-weight: 600; border: none; padding: 0.7rem;
    }
    .stButton>button:hover { background-color: #2e7d32; }
    .footer {
        margin-top: 2rem;
        padding: 1rem;
        text-align: center;
        font-size: 0.9rem;
        color: #33691e;
        border-top: 1px solid #c8e6c9;
    }
</style>
""", unsafe_allow_html=True)

# --- Session State Initialization ---
if "total_score" not in st.session_state:
    st.session_state.total_score = 0
    st.session_state.completed_systems = []
    for system in ["solar", "wind", "hydro", "biomass"]:
        st.session_state[f"{system}_score"] = 0
        st.session_state[f"{system}_completed"] = False

# --- Sidebar Logo & Progress ---
st.sidebar.image(
    "https://upload.wikimedia.org/wikipedia/en/thumb/7/7a/SRM_Institute_of_Science_and_Technology_Logo.svg/1200px-SRM_Institute_of_Science_and_Technology_Logo.svg.png",
    use_container_width=True
)
st.sidebar.title("📈 Progress Tracker")
st.session_state.total_score = (
    st.session_state["solar_score"]
    + st.session_state["wind_score"]
    + st.session_state["hydro_score"]
    + st.session_state["biomass_score"]
)
st.sidebar.metric("Total Score", f"{st.session_state.total_score} / 40")
st.sidebar.progress(len(st.session_state.completed_systems) / 4)
st.sidebar.markdown(f"**Systems Mastered:** {len(st.session_state.completed_systems)} / 4")

if st.sidebar.button("🔴 Reset Progress"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# --- Header Section ---
st.markdown("""
<div class="header-container">
    <h1>🌍 EcoEngineer: Core Concepts</h1>
    <p>A foundational challenge for future engineers – learn renewable energy through interactive quizzes & diagrams.</p>
</div>
""", unsafe_allow_html=True)

# --- Direction Box (top of homepage) ---
st.info("ℹ️ Use the **sidebar** to navigate: Start with **Solar PV**, then continue to **Wind**, **Hydro**, and **Biomass** step by step.")

# --- System Selection ---
st.markdown("## ⚡ Select a System to Explore")

systems = [
    {"name": "Solar PV System", "icon": "🔆", "file": "pages/1_Solar_PV_System.py"},
    {"name": "Wind Energy", "icon": "🌪️", "file": "pages/2_Wind_Energy.py"},
    {"name": "Hydroelectric Power", "icon": "💧", "file": "pages/3_Hydroelectric_Power.py"},
    {"name": "Biomass Energy", "icon": "🌱", "file": "pages/4_Biomass_Energy.py"},
]

rows = st.columns(2)
for i, sys in enumerate(systems):
    with rows[i % 2]:
        completed = sys["name"] in st.session_state.completed_systems
        status = "✅" if completed else "▶️"
        st.markdown(f"""
        <div class="system-card">
            <h3>{sys['icon']} {sys['name']} {status}</h3>
            <a href="{sys['file']}" target="_self">
                <button>Start Challenge</button>
            </a>
        </div>
        """, unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<div class="footer">
    🚀 Built with ❤️ for Future Engineers | EcoEngineer™ 2025
</div>
""", unsafe_allow_html=True)
