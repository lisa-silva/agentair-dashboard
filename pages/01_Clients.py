import streamlit as st
import pandas as pd
from datetime import datetime

st.title("👥 Client Management")

# Add new client form
with st.expander("➕ Add New Client", expanded=False):
    with st.form("new_client"):
        col1, col2 = st.columns(2)
        with col1:
            business_name = st.text_input("Business Name *")
            contact_name = st.text_input("Contact Name")
            email = st.text_input("Email *")
        with col2:
            phone = st.text_input("Phone")
            website = st.text_input("Website URL *")
            business_type = st.selectbox(
                "Business Type",
                ["Plumbing", "Electrical", "Roofing", "HVAC", "Landscaping", 
                 "Dental", "Medical", "Legal", "Restaurant", "Retail", "Other"]
            )
        
        address = st.text_area("Business Address")
        
        submitted = st.form_submit_button("Save Client")
        if submitted and business_name and website:
            new_client = {
                "id": len(st.session_state.clients) + 1,
                "business_name": business_name,
                "contact_name": contact_name,
                "email": email,
                "phone": phone,
                "website": website,
                "business_type": business_type,
                "address": address,
                "added_date": datetime.now().strftime("%Y-%m-%d"),
                "status": "active"
            }
            st.session_state.clients.append(new_client)
            st.success(f"✅ {business_name} added successfully!")
            st.rerun()

# Client list
st.subheader("Your Clients")

if st.session_state.clients:
    # Convert to DataFrame for display
    df = pd.DataFrame(st.session_state.clients)
    
    # Action buttons for each client
    for idx, client in enumerate(st.session_state.clients):
        with st.container(border=True):
            col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 1])
            with col1:
                st.markdown(f"**{client['business_name']}**")
                st.caption(client['website'])
            with col2:
                st.markdown(f"📧 {client['email']}")
            with col3:
                st.markdown(f"📱 {client.get('phone', '—')}")
            with col4:
                st.markdown(f"🏷️ {client['business_type']}")
            with col5:
                if st.button("🔍 Audit", key=f"audit_{idx}"):
                    st.switch_page("pages/02_Audits.py")
                if st.button("🛠️ Fix", key=f"fix_{idx}"):
                    st.switch_page("pages/03_Schema_Fixer.py")
else:
    st.info("No clients yet. Add your first client to get started.")
