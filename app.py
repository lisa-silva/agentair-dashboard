import streamlit as st
from utils.auth import check_password
import hmac

st.set_page_config(
    page_title="AgentAir Agency Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Simple authentication (replace with real auth later)
def check_password():
    """Returns `True` if the user had the correct password."""
    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store password
        else:
            st.session_state["password_correct"] = False

    if st.session_state.get("password_correct", False):
        return True

    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    return False

if not check_password():
    st.stop()

# Sidebar navigation
st.sidebar.image("https://via.placeholder.com/150x50?text=AgentAir", use_container_width=True)
st.sidebar.markdown("## Agency Dashboard")
st.sidebar.markdown("---")

# Initialize session state for clients if not exists
if 'clients' not in st.session_state:
    st.session_state.clients = []

# Main dashboard
st.title("🛡️ AgentAir Agency Dashboard")
st.markdown("Welcome back! Here's your overview.")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Clients", len(st.session_state.clients))
with col2:
    st.metric("Audits This Month", "12")
with col3:
    st.metric "Fixes Applied", "8")
with col4:
    st.metric("Monthly Revenue", f"${len(st.session_state.clients) * 99}")
