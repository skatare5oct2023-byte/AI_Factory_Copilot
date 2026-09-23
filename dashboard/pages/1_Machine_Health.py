import streamlit as st


st.set_page_config(
    page_title="Machine Health",
    page_icon="❤️",
    layout="wide"
)


st.title("❤️ Machine Health Monitoring")

st.write(
    "Monitor the health status and condition of factory machines."
)


# Example metrics
col1, col2, col3 = st.columns(3)

col1.metric(
    "Machine Status",
    "Healthy"
)

col2.metric(
    "Health Score",
    "92%"
)

col3.metric(
    "Risk Level",
    "Low"
)


st.subheader("Machine Monitoring")

st.info(
    "Machine health prediction will be connected here."
)