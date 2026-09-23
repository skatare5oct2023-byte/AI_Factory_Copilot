import streamlit as st


st.set_page_config(
    page_title="Maintenance Report",
    page_icon="📄",
    layout="wide"
)


st.title("📄 Automated Maintenance Report")

st.write(
    "Generate AI-powered maintenance reports for factory machines."
)


machine = st.selectbox(
    "Select Machine",
    [
        "Mixing Machine",
        "Coating Machine",
        "Drying Oven",
        "Cell Assembly Machine"
    ]
)


if st.button("Generate Report"):

    st.success(
        f"Maintenance report generated for {machine}"
    )

    st.write("### Report")

    st.write(
        "Machine Status: Healthy"
    )

    st.write(
        "Recommended Action: Continue regular preventive maintenance."
    )