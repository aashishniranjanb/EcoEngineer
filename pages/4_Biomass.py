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
st.set_page_config("🌱 Biomass Energy", layout="wide")
st.markdown("""
<style>
.quiz-container { background:#fff;padding:2rem;border-radius:10px;box-shadow:0 4px 12px rgba(0,0,0,0.1); }
.stButton>button { background:#4CAF50;color:#fff; }
</style>
""", unsafe_allow_html=True)

# State Init
def init_bio():
    st.session_state.biomass_stage=1
    st.session_state.biomass_score=0
    st.session_state.biomass_completed=False
    st.session_state.biomass_hint=""
if 'biomass_stage' not in st.session_state:
    init_bio()

# Header
st.title("🌱 Biomass Energy System")
if st.button("← Back to Home"): st.experimental_set_query_params()

# Content
st.subheader("How It Works")
st.markdown("""
1. **Fuel** burned in **Furnace** → heats **Boiler** → steam.  
2. Steam spins **Turbine** → drives **Generator** → electricity.
""")

st.subheader("Diagram")
st.graphviz_chart("""
digraph {
  Fuel -> Furnace -> Boiler -> Turbine -> Generator -> Grid;
}
""")

st.subheader("Key Facts")
st.info("Efficiency: 20–40%; CHP >80%; carbon-neutral cycle; fuels: wood, residues.")

# --- Stage 1 ---
if st.session_state.biomass_stage==1:
    with st.container():
        st.markdown("### Stage 1: Process Order (2 pts)")
        comps=["Generator","Furnace","Boiler","Turbine"]
        correct=["Furnace","Boiler","Turbine","Generator"]
        order=[]
        cols=st.columns(4)
        for i,c in enumerate(cols):
            order.append(c.selectbox(f"{i+1}",comps,key=f"b1_{i}"))
        if st.button("Check Order",key="b1"):
            if order==correct:
                st.success("+2 pts")
                st.session_state.biomass_score+=2
                st.session_state.biomass_stage=2
            else:
                st.error("Trace heat→steam→motion→electricity")
                st.session_state.biomass_hint="Hint: Burn→steam→spin→generate"
        if st.session_state.biomass_hint: st.warning(st.session_state.biomass_hint)
else:
    st.markdown("✅ Stage 1 Complete")

# --- Stage 2 ---
if st.session_state.biomass_stage==2:
    with st.container():
        st.markdown("### Stage 2: Concept Question (2 pts)")
        st.write("Why is dry fuel more efficient than wet fuel?")
        opts=["Burns hotter","Less latent heat loss","Easier transport","Higher C content"]
        ans=st.radio("",opts,key="b2")
        if st.button("Submit",key="b2b"):
            if ans=="Less latent heat loss":
                st.success("+2 pts")
                st.session_state.biomass_score+=2
                st.session_state.biomass_stage=3
                st.session_state.biomass_hint=""
            else:
                st.error("Consider energy to evaporate water")
                st.session_state.biomass_hint="Hint: Latent heat of vaporization"
        if st.session_state.biomass_hint: st.warning(st.session_state.biomass_hint)
else:
    st.markdown("✅ Stage 2 Complete")

# --- Stage 3 ---
if st.session_state.biomass_stage==3:
    with st.container():
        st.markdown("### Stage 3: Efficiency Calc (1 pt)")
        st.write("200 MW input @ 25% → output?")
        val=st.number_input("MW:",0,200,step=1,key="b3")
        if st.button("Check",key="b3b"):
            if abs(val-50)<1:
                st.success("+1 pt")
                st.session_state.biomass_score+=1
                st.session_state.biomass_stage=4
            else:
                st.error("Output = Input × Efficiency")
                st.session_state.biomass_hint="Hint: 200×0.25"
        if st.session_state.biomass_hint: st.warning(st.session_state.biomass_hint)
else:
    st.markdown("✅ Stage 3 Complete")

# --- Stage 4: Concept (2 pts) ---
if st.session_state.biomass_stage==4:
    with st.container():
        st.markdown("### Stage 4: Concept Question (2 pts)")
        q="Which of these is considered a 'second-generation' biofuel?"
        st.write(q)
        opts=["Corn ethanol","Palm oil","Wood pellets from forestry waste","Sugarcane"]
        ans=st.radio("",opts,key="b4_ans")
        if st.button("Submit",key="b4"):
            if ans==opts[2]:
                st.success("Correct! +2 pts")
                st.session_state.biomass_score+=2
                st.session_state.biomass_stage=5
            else:
                st.error("Check biofuel classification.")
                st.session_state.biomass_hint="Hint: 2nd-gen comes from non-food waste biomass."
        if st.session_state.biomass_hint: st.warning(st.session_state.biomass_hint)
else:
    if st.session_state.biomass_stage>4: st.markdown("✅ Stage 4 Complete")

# --- Stage 5: Application (2 pts) ---
if st.session_state.biomass_stage==5:
    with st.container():
        st.markdown("### Stage 5: Application Question (2 pts)")
        q="What is the primary advantage of a Combined Heat and Power (CHP) biomass plant?"
        st.write(q)
        opts=["It uses less fuel","It is easier to build","It has a much higher overall efficiency","It produces no emissions"]
        ans=st.radio("",opts,key="b5_ans")
        if st.button("Submit",key="b5"):
            if ans==opts[2]:
                st.success("Correct! +2 pts")
                st.session_state.biomass_score+=2
                st.session_state.biomass_stage=6
            else:
                st.error("Think about efficiency improvements.")
                st.session_state.biomass_hint="Hint: CHP uses waste heat to raise total efficiency."
        if st.session_state.biomass_hint: st.warning(st.session_state.biomass_hint)
else:
    if st.session_state.biomass_stage>5: st.markdown("✅ Stage 5 Complete")

# --- Stage 6: Bonus Calc (1 pt) ---
if st.session_state.biomass_stage==6:
    with st.container():
        st.markdown("### Stage 6: Bonus Calculation (1 pt)")
        st.write("If 100 kg of biomass contains 2000 MJ of energy, and its moisture content is 20%, what is the energy content of the dry biomass?")
        val=st.number_input("MJ:",0,5000,step=50,key="b6_val")
        if st.button("Check",key="b6"):
            if abs(val - 2500)<10:
                st.success("Correct! +1 pt")
                st.session_state.biomass_score+=1
                st.session_state.biomass_completed=True
                st.session_state.completed_systems.append("Biomass Energy")
                st.balloons()
            else:
                st.error("Recheck calculation.")
                st.session_state.biomass_hint="Hint: Energy_dry = 2000 / 0.8"
        if st.session_state.biomass_hint: st.warning(st.session_state.biomass_hint)
else:
    if st.session_state.biomass_completed: st.markdown("✅ Stage 6 Complete")

# --- Completion ---
if st.session_state.biomass_completed:
    st.success(f"🎉 Completed! Score: {st.session_state.biomass_score}/10")
