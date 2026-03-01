import streamlit as st

st.title("⚙️ Agency Settings")

with st.form("agency_profile"):
    col1, col2 = st.columns(2)
    with col1:
        agency_name = st.text_input("Agency Name")
        agency_email = st.text_input("Contact Email")
    with col2:
        agency_logo = st.text_input("Logo URL")
        white_label = st.checkbox("Enable White-Label Mode (hide AgentAir branding)")
    
    st.subheader("White-Label Settings")
    if white_label:
        st.text_input("Your Brand Name", placeholder="Your Agency Name")
        st.text_input("Report Footer Text", placeholder="Powered by Your Agency")
    
    st.form_submit_button("Save Settings")
