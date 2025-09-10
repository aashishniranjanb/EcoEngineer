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
st.set_page_config("💧 Hydroelectric Power", layout="wide")
st.markdown("""
<style>
.quiz-container { background:#fff;padding:2rem;border-radius:10px;box-shadow:0 4px 12px rgba(0,0,0,0.1); }
.stButton>button { background:#2196F3;color:#fff; }
</style>
""", unsafe_allow_html=True)

# State Init
def init_hydro():
    st.session_state.hydro_stage=1
    st.session_state.hydro_score=0
    st.session_state.hydro_completed=False
    st.session_state.hydro_hint=""
if 'hydro_stage' not in st.session_state:
    init_hydro()

# Header
st.title("💧 Hydroelectric Power System")
if st.button("← Back to Home"): st.experimental_set_query_params()

# Content
st.subheader("How It Works")
st.markdown("""
1. **Reservoir** stores water (PE=mgh).  
2. Water flows through **Penstock** → **Turbine** spins.  
3. **Generator** produces electricity; water exits via **Tailrace**.
""")

st.subheader("Diagram")
st.graphviz_chart("""
digraph {
  Reservoir -> Penstock -> Turbine -> Generator -> Grid;
  Turbine -> Tailrace;
}
""")

st.subheader("Key Facts")
st.info("Efficiency: 85–95%; PE=mgh; applications: dams, run-of-river, pumped storage.")

# --- Stage 1 ---
if st.session_state.hydro_stage==1:
    with st.container():
        st.markdown("### Stage 1: Flow Order (2 pts)")
        comps=["Turbine","Reservoir","Penstock","Tailrace"]
        correct=["Reservoir","Penstock","Turbine","Tailrace"]
        order=[]
        cols=st.columns(4)
        for i,c in enumerate(cols):
            order.append(c.selectbox(f"{i+1}",comps,key=f"h1_{i}"))
        if st.button("Check Order",key="h1"):
            if order==correct:
                st.success("+2 pts")
                st.session_state.hydro_score+=2
                st.session_state.hydro_stage=2
            else:
                st.error("Trace water from stored→exit")
                st.session_state.hydro_hint="Hint: Start at reservoir, end at tailrace"
        if st.session_state.hydro_hint: st.warning(st.session_state.hydro_hint)
else:
    st.markdown("✅ Stage 1 Complete")

# --- Stage 2 ---
if st.session_state.hydro_stage==2:
    with st.container():
        st.markdown("### Stage 2: Concept Question (2 pts)")
        st.write("Double dam height → power?")
        opts=["Same","2×","4×","½×"]
        ans=st.radio("",opts,key="h2")
        if st.button("Submit",key="h2b"):
            if ans=="2×":
                st.success("+2 pts")
                st.session_state.hydro_score+=2
                st.session_state.hydro_stage=3
                st.session_state.hydro_hint=""
            else:
                st.error("Power∝head")
                st.session_state.hydro_hint="Hint: PE=mgh → if h doubles, PE doubles"
        if st.session_state.hydro_hint: st.warning(st.session_state.hydro_hint)
else:
    st.markdown("✅ Stage 2 Complete")

# --- Stage 3 ---
if st.session_state.hydro_stage==3:
    with st.container():
        st.markdown("### Stage 3: Energy Calc (1 pt)")
        st.write("1000 kg @ 50 m; g=9.8 → PE?")
        val=st.number_input("Joules:",0,1000000,step=100,key="h3")
        if st.button("Check",key="h3b"):
            if abs(val - 1000*9.8*50)<100:
                st.success("+1 pt")
                st.session_state.hydro_score+=1
                st.session_state.hydro_stage=4
            else:
                st.error("PE=mgh")
                st.session_state.hydro_hint="Hint: 1000×9.8×50"
        if st.session_state.hydro_hint: st.warning(st.session_state.hydro_hint)
else:
    st.markdown("✅ Stage 3 Complete")

# --- Stage 4: Application (2 pts) ---
if st.session_state.hydro_stage==4:
    with st.container():
        st.markdown("### Stage 4: Application Question (2 pts)")
        q="What is a 'run-of-river' hydroelectric plant?"
        st.write(q)
        opts=["A plant that uses a reservoir",
              "A small plant that does not use a large dam",
              "A plant for water purification",
              "A plant that only works in winter"]
        ans=st.radio("",opts,key="h4_ans")
        if st.button("Submit",key="h4"):
            if ans==opts[1]:
                st.success("Correct! +2 pts")
                st.session_state.hydro_score+=2
                st.session_state.hydro_stage=5
            else:
                st.error("Think about small-scale systems.")
                st.session_state.hydro_hint="Hint: Not all hydro needs massive dams."
        if st.session_state.hydro_hint: st.warning(st.session_state.hydro_hint)
else:
    if st.session_state.hydro_stage>4: st.markdown("✅ Stage 4 Complete")

# --- Stage 5: Concept (2 pts) ---
if st.session_state.hydro_stage==5:
    with st.container():
        st.markdown("### Stage 5: Concept Question (2 pts)")
        q="In the context of hydropower, what does the term 'head' refer to?"
        st.write(q)
        opts=["The length of the dam","The volume of the reservoir","The vertical height difference the water falls","The water flow rate"]
        ans=st.radio("",opts,key="h5_ans")
        if st.button("Submit",key="h5"):
            if ans==opts[2]:
                st.success("Correct! +2 pts")
                st.session_state.hydro_score+=2
                st.session_state.hydro_stage=6
            else:
                st.error("Check hydro power formula P∝h.")
                st.session_state.hydro_hint="Hint: It's the height water falls."
        if st.session_state.hydro_hint: st.warning(st.session_state.hydro_hint)
else:
    if st.session_state.hydro_stage>5: st.markdown("✅ Stage 5 Complete")

# --- Stage 6: Bonus Calc (1 pt) ---
if st.session_state.hydro_stage==6:
    with st.container():
        st.markdown("### Stage 6: Bonus Calculation (1 pt)")
        st.write("A plant generates 50 MW. If it operates for 2 hours, how much energy (in MWh)?")
        val=st.number_input("MWh:",0,500,step=10,key="h6_val")
        if st.button("Check",key="h6"):
            if abs(val - 100)<1:
                st.success("Correct! +1 pt")
                st.session_state.hydro_score+=1
                st.session_state.hydro_completed=True
                st.session_state.completed_systems.append("Hydroelectric Power")
                st.balloons()
            else:
                st.error("Use E=P×t")
                st.session_state.hydro_hint="Hint: 50×2=100 MWh"
        if st.session_state.hydro_hint: st.warning(st.session_state.hydro_hint)
else:
    if st.session_state.hydro_completed: st.markdown("✅ Stage 6 Complete")

# --- Completion ---
if st.session_state.hydro_completed:
    st.success(f"🎉 Completed! Score: {st.session_state.hydro_score}/10")
