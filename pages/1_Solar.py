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


# --- Page Config ---
st.set_page_config(page_title="🔆 Solar PV System", layout="wide")

# --- Styling ---
st.markdown("""
<style>
    body { background-color: #f0f4f8; }
    .quiz-container { background: #fff; padding: 2rem; border-radius: 10px; margin-top: 1rem; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
    .stButton>button { background-color: #FFC107; color: black; }
</style>
""", unsafe_allow_html=True)

# --- State Init ---
def init_solar():
    st.session_state.solar_stage = 1
    st.session_state.solar_score = 0
    st.session_state.solar_completed = False
    st.session_state.solar_hint = ""
if 'solar_stage' not in st.session_state:
    init_solar()

# --- Header ---
st.title("🔆 Solar Photovoltaic (PV) System")
if st.button("← Back to Home"): st.experimental_set_query_params()

# --- Content ---
st.subheader("How It Works")
st.markdown("""
A PV system converts sunlight into electricity via the *photovoltaic effect*.  
1. **PV Panel** absorbs photons → generates DC current.  
2. **Charge Controller** prevents battery overcharge.  
3. **Battery** stores energy.  
4. **Inverter** converts DC → AC for appliances.
""")

st.subheader("System Diagram")
st.graphviz_chart("""
digraph {
  node [shape=box, style=rounded];
  Sunlight -> PV_Panel -> Charge_Controller -> Battery -> Inverter -> AC_Load;
}
""")

st.subheader("Key Facts")
st.info("""
- Efficiency: **18–23%**  
- Applications: Rooftop, solar farms, satellites  
- Nominal Voltages: 12V, 24V, 48V DC
""")

# --- Stage 1: Arrangement (2 pts) ---
if st.session_state.solar_stage == 1:
    with st.container():
        st.markdown("### Stage 1: Component Arrangement (2 pts)")
        order = []
        comps = ["Inverter","PV Panel","Charge Controller","Battery"]
        correct = ["PV Panel","Charge Controller","Battery","Inverter"]
        cols = st.columns(4)
        for i,c in enumerate(cols):
            order.append(c.selectbox(f"{i+1}", comps, key=f"s1_{i}"))
        if st.button("Check Arrangement"):
            if order==correct:
                st.success("Correct! +2 pts")
                st.session_state.solar_score+=2
                st.session_state.solar_stage=2
            else:
                st.error("Wrong order.")
                st.session_state.solar_hint="Hint: Capture → Control → Store → Convert"
        if st.session_state.solar_hint:
            st.warning(st.session_state.solar_hint)
else:
    st.markdown("✅ Stage 1 Complete")

# --- Stage 2: Concept (2 pts) ---
if st.session_state.solar_stage==2:
    with st.container():
        st.markdown("### Stage 2: Concept Question (2 pts)")
        q="If sunlight intensity doubles (T constant), what happens?"
        st.write(q)
        opts=["Voltage doubles","Current doubles","Both halve","No change"]
        ans=st.radio("",opts,key="s2_ans")
        if st.button("Submit Answer",key="s2"):
            if ans==opts[1]:
                st.success("Correct! +2 pts")
                st.session_state.solar_score+=2
                st.session_state.solar_stage=3
                st.session_state.solar_hint=""
            else:
                st.error("Think photons → electrons")
                st.session_state.solar_hint="Hint: More photons → more electron flow"
        if st.session_state.solar_hint:
            st.warning(st.session_state.solar_hint)
else:
    st.markdown("✅ Stage 2 Complete")

# --- Stage 3: Calculation (1 pt) ---
if st.session_state.solar_stage==3:
    with st.container():
        st.markdown("### Stage 3: Quick Calculation (1 pt)")
        st.write("300W panel × 5 h → ? kWh")
        val=st.number_input("kWh:",0.0,10.0,step=0.1,key="s3_val")
        if st.button("Check",key="s3"):
            if abs(val - 1.5) < 0.01:
                st.success("Correct! +1 pt")
                st.session_state.solar_score+=1
                st.session_state.solar_stage=4
                st.session_state.solar_hint=""
            else:
                st.error("Energy=Power×Time; convert Wh→kWh")
                st.session_state.solar_hint="Hint: 300×5=1500 Wh → 1.5 kWh"
        if st.session_state.solar_hint:
            st.warning(st.session_state.solar_hint)
else:
    st.markdown("✅ Stage 3 Complete")

# --- Stage 4: Application (2 pts) ---
if st.session_state.solar_stage==4:
    with st.container():
        st.markdown("### Stage 4: Application Question (2 pts)")
        q="Why are solar panels often tilted at an angle instead of being flat?"
        st.write(q)
        opts=["To drain water","To prevent dust buildup","To maximize sunlight capture throughout the day","To reduce wind load"]
        ans=st.radio("",opts,key="s4_ans")
        if st.button("Submit",key="s4"):
            if ans==opts[2]:
                st.success("Correct! +2 pts")
                st.session_state.solar_score+=2
                st.session_state.solar_stage=5
            else:
                st.error("Not quite right.")
                st.session_state.solar_hint="Hint: Angle of incidence matters for energy capture."
        if st.session_state.solar_hint: st.warning(st.session_state.solar_hint)
else:
    if st.session_state.solar_stage>4: st.markdown("✅ Stage 4 Complete")

# --- Stage 5: Concept (2 pts) ---
if st.session_state.solar_stage==5:
    with st.container():
        st.markdown("### Stage 5: Concept Question (2 pts)")
        q="What is the primary function of an inverter in a PV system?"
        st.write(q)
        opts=["To convert AC → DC","To store energy","To step up voltage","To convert DC → AC"]
        ans=st.radio("",opts,key="s5_ans")
        if st.button("Submit",key="s5"):
            if ans==opts[3]:
                st.success("Correct! +2 pts")
                st.session_state.solar_score+=2
                st.session_state.solar_stage=6
            else:
                st.error("Check the role of the inverter.")
                st.session_state.solar_hint="Hint: Appliances need AC power."
        if st.session_state.solar_hint: st.warning(st.session_state.solar_hint)
else:
    if st.session_state.solar_stage>5: st.markdown("✅ Stage 5 Complete")

# --- Stage 6: Bonus Calc (1 pt) ---
if st.session_state.solar_stage==6:
    with st.container():
        st.markdown("### Stage 6: Bonus Calculation (1 pt)")
        st.write("A solar farm has 100 panels, each rated at 400W. What is the total nominal power output (in kW)?")
        val=st.number_input("kW:",0.0,100.0,step=1.0,key="s6_val")
        if st.button("Check",key="s6"):
            if abs(val - 40) < 0.01:
                st.success("Correct! +1 pt")
                st.session_state.solar_score+=1
                st.session_state.solar_completed=True
                st.session_state.completed_systems.append("Solar PV System")
                st.balloons()
            else:
                st.error("Recheck: 100×400 W → ?")
                st.session_state.solar_hint="Hint: 100×400=40000 W → 40 kW"
        if st.session_state.solar_hint: st.warning(st.session_state.solar_hint)
else:
    if st.session_state.solar_completed: st.markdown("✅ Stage 6 Complete")

# --- Completion ---
if st.session_state.solar_completed:
    st.success(f"🎉 Completed! Score: {st.session_state.solar_score}/10")
    if "Solar Specialist" not in st.session_state.achievements:
        st.session_state.achievements.append("Solar Specialist")
    if st.button("← Back to Home"):
        st.experimental_set_query_params()