import streamlit as st

def placement_prediction():

    st.header("🤖 AI Placement Prediction")

    cgpa = st.number_input(
        "Enter CGPA",
        min_value=0.0,
        max_value=10.0,
        step=0.1
    )

    python_skill = st.checkbox("Python")
    sql_skill = st.checkbox("SQL")
    dsa_skill = st.checkbox("DSA")

    if st.button("Predict"):

        score = 0

        if cgpa >= 8.5:
            score += 3
        elif cgpa >= 7:
            score += 2
        else:
            score += 1

        if python_skill:
            score += 1

        if sql_skill:
            score += 1

        if dsa_skill:
            score += 1

        if score >= 6:
            st.success("🟢 High Placement Chance")

        elif score >= 4:
            st.warning("🟡 Moderate Placement Chance")

        else:
            st.error("🔴 Improve Skills for Better Placement")