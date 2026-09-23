import streamlit as st

st.set_page_config(
    page_title="AI Factory Operations Copilot",
    page_icon="🏭",
    layout="wide"
)

st.title("🏭 AI Factory Operations Copilot")

st.write(
    "AI-powered Smart Manufacturing Platform for EV Battery Production"
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Machines",
    "12"
)

col2.metric(
    "Healthy Machines",
    "10"
)

col3.metric(
    "Warning",
    "2"
)

col4.metric(
    "Production Efficiency",
    "94%"
)

st.divider()

st.subheader("System Overview")

st.info(
    "Use the navigation menu to access Machine Health, AI Assistant, Production Analytics, and Maintenance Reports."
)