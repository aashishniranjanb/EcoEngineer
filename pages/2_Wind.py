import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="EcoEngineer Challenge", page_icon="🌱", layout="wide")

# --- Green Theme Styling ---
st.markdown("""
<style>
    body { background-color: #f4faf4; font-family: "Segoe UI", Arial, sans-serif; }
    .header-container {
        background: linear-gradient(90deg, #2e7d32, #66bb6a);
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.15);
        text-align: center;
        margin-bottom: 1.2rem;
        color: white;
    }
    .header-container h1 { font-weight: 800; font-size: 2rem; margin:0; }
    .header-container p { margin:0.3rem 0 0 0; opacity:0.95; font-size: 1rem; }
    .stButton>button {
        background-color: #388e3c; color: #fff; border-radius: 8px;
        font-weight: 600; border: none; padding: 0.6rem 1.2rem;
    }
    .stButton>button:hover { background-color: #2e7d32; }
</style>
""", unsafe_allow_html=True)

# safe init for pages (paste near top of every pages/*.py)
if "achievements" not in st.session_state:
    st.session_state.achievements = []
# keep existing per-page stage initialization as you already have it


# Config & Style
st.set_page_config("🌪️ Wind Energy", layout="wide")
st.markdown("""
<style>
.quiz-container { background:#fff;padding:2rem;border-radius:10px;box-shadow:0 4px 12px rgba(0,0,0,0.1); }
.stButton>button { background:#03A9F4;color:#fff; }
</style>
""", unsafe_allow_html=True)

# State Init
def init_wind():
    st.session_state.wind_stage=1
    st.session_state.wind_score=0
    st.session_state.wind_completed=False
    st.session_state.wind_hint=""
if 'wind_stage' not in st.session_state:
    init_wind()

# Header
st.title("🌪️ Wind Energy System")
if st.button("← Back to Home"): st.experimental_set_query_params()

# Content
st.subheader("How It Works")
st.markdown("""
1. **Blades** capture wind → spin shaft.  
2. **Gearbox** ups speed → **Generator** produces AC.  
3. **Transformer** steps up voltage → grid.
""")

st.subheader("Diagram")
st.graphviz_chart("""
digraph {
  Wind -> Blades -> Gearbox -> Generator -> Transformer -> Grid;
}
""")

st.subheader("Key Facts")
st.info("Theoretical max efficiency 59.3% (Betz); real 35–45%; Power ∝ wind speed³.")

# --- Stage 1 ---
if st.session_state.wind_stage==1:
    with st.container():
        st.markdown("### Stage 1: Powertrain Order (2 pts)")
        comps=["Generator","Rotor Blades","Gearbox","Transformer"]
        correct=["Rotor Blades","Gearbox","Generator","Transformer"]
        order=[]
        cols=st.columns(4)
        for i,c in enumerate(cols):
            order.append(c.selectbox(f"{i+1}",comps,key=f"w1_{i}"))
        if st.button("Check Order",key="w1"):
            if order==correct:
                st.success("+2 pts")
                st.session_state.wind_score+=2
                st.session_state.wind_stage=2
            else:
                st.error("Trace from wind→grid")
                st.session_state.wind_hint="Hint: Mechanical capture→speed change→electrical→voltage"
        if st.session_state.wind_hint: st.warning(st.session_state.wind_hint)
else:
    st.markdown("✅ Stage 1 Complete")

# --- Stage 2 ---
if st.session_state.wind_stage==2:
    with st.container():
        st.markdown("### Stage 2: Physics Question (2 pts)")
        st.write("Doubling wind speed → new power?")
        opts=["2×","4×","8×","16×"]
        ans=st.radio("",opts,key="w2")
        if st.button("Submit",key="w2b"):
            if ans=="8×":
                st.success("+2 pts")
                st.session_state.wind_score+=2
                st.session_state.wind_stage=3
                st.session_state.wind_hint=""
            else:
                st.error("Use P∝v³")
                st.session_state.wind_hint="Hint: v² in KE and additional v in mass flow"
        if st.session_state.wind_hint: st.warning(st.session_state.wind_hint)
else:
    st.markdown("✅ Stage 2 Complete")

# --- Stage 3 ---
if st.session_state.wind_stage==3:
    with st.container():
        st.markdown("### Stage 3: Efficiency Calc (1 pt)")
        st.write("1000 kW theoretical × 40% = ? kW")
        val=st.number_input("kW:",0,1000,step=10,key="w3")
        if st.button("Check",key="w3b"):
            if abs(val-400)<1:
                st.success("+1 pt")
                st.session_state.wind_score+=1
                st.session_state.wind_stage=4
            else:
                st.error("P_actual=P_theoretical×η")
                st.session_state.wind_hint="Hint: 1000×0.4"
        if st.session_state.wind_hint: st.warning(st.session_state.wind_hint)
else:
    st.markdown("✅ Stage 3 Complete")

# --- Stage 4: Application (2 pts) ---
if st.session_state.wind_stage==4:
    with st.container():
        st.markdown("### Stage 4: Application Question (2 pts)")
        q="Why are wind turbines typically shut down during extremely high wind speeds?"
        st.write(q)
        opts=["To save wear and tear on the gearbox",
              "To prevent over-voltage to the grid",
              "To avoid structural damage to the blades and tower",
              "To reduce noise pollution"]
        ans=st.radio("",opts,key="w4_ans")
        if st.button("Submit",key="w4"):
            if ans==opts[2]:
                st.success("Correct! +2 pts")
                st.session_state.wind_score+=2
                st.session_state.wind_stage=5
            else:
                st.error("Think about safety limits.")
                st.session_state.wind_hint="Hint: Blades & towers can fail under extreme loads."
        if st.session_state.wind_hint: st.warning(st.session_state.wind_hint)
else:
    if st.session_state.wind_stage>4: st.markdown("✅ Stage 4 Complete")

# --- Stage 5: Concept (2 pts) ---
if st.session_state.wind_stage==5:
    with st.container():
        st.markdown("### Stage 5: Concept Question (2 pts)")
        q="What is the name of the aerodynamic principle that allows a wind turbine's blades to spin?"
        st.write(q)
        opts=["Bernoulli's principle","Pascal's law","Archimedes' principle","Newton's third law"]
        ans=st.radio("",opts,key="w5_ans")
        if st.button("Submit",key="w5"):
            if ans==opts[0]:
                st.success("Correct! +2 pts")
                st.session_state.wind_score+=2
                st.session_state.wind_stage=6
            else:
                st.error("Recheck fluid dynamics basics.")
                st.session_state.wind_hint="Hint: It’s the same principle that makes airplanes fly."
        if st.session_state.wind_hint: st.warning(st.session_state.wind_hint)
else:
    if st.session_state.wind_stage>5: st.markdown("✅ Stage 5 Complete")

# --- Stage 6: Bonus Calc (1 pt) ---
if st.session_state.wind_stage==6:
    with st.container():
        st.markdown("### Stage 6: Bonus Calculation (1 pt)")
        st.write("A turbine’s output is 2 MW at 10 m/s wind. What would be its output at 5 m/s (same efficiency)?")
        val=st.number_input("MW:",0.0,5.0,step=0.1,key="w6_val")
        if st.button("Check",key="w6"):
            if abs(val - 0.25) < 0.01:
                st.success("Correct! +1 pt")
                st.session_state.wind_score+=1
                st.session_state.wind_completed=True
                st.session_state.completed_systems.append("Wind Energy")
                st.balloons()
            else:
                st.error("Use cubic relation: P∝v³")
                st.session_state.wind_hint="Hint: (5/10)³ × 2 MW"
        if st.session_state.wind_hint: st.warning(st.session_state.wind_hint)
else:
    if st.session_state.wind_completed: st.markdown("✅ Stage 6 Complete")

# --- Completion ---
if st.session_state.wind_completed:
    st.success(f"🎉 Completed! Score: {st.session_state.wind_score}/10")
