import streamlit as st
from utils.schema_fixer import LocalBusinessSchemaGenerator

st.title("🛠️ Schema Fixer Tool")

# Client selector
if st.session_state.clients:
    client_names = [c['business_name'] for c in st.session_state.clients]
    selected = st.selectbox("Select Client to Fix", client_names)
    
    client = next(c for c in st.session_state.clients if c['business_name'] == selected)
    
    st.markdown(f"**Generating schema for:** {client['business_name']}")
    
    # Pre-fill from client data
    with st.form("schema_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            business_name = st.text_input("Business Name", value=client['business_name'])
            service_type = st.selectbox(
                "Business Type",
                ["plumber", "electrician", "roofer", "hvac", "contractor", 
                 "dentist", "lawyer", "restaurant", "general"],
                index=9  # default general
            )
            phone = st.text_input("Phone", value=client.get('phone', ''))
            url = st.text_input("Website", value=client['website'])
        
        with col2:
            email = st.text_input("Email", value=client.get('email', ''))
            street = st.text_input("Street Address")
            city = st.text_input("City")
            state = st.text_input("State", max_chars=2)
            zip_code = st.text_input("ZIP")
        
        submitted = st.form_submit_button("🚀 Generate Schema")
        
        if submitted:
            business_data = {
                "name": business_name,
                "service_type": service_type,
                "phone": phone,
                "url": url,
                "email": email,
                "address": {
                    "street": street,
                    "city": city,
                    "state": state,
                    "zip": zip_code,
                    "country": "US"
                },
                "hours": {},  # Add hours UI later
                "price_range": "$$"
            }
            
            generator = LocalBusinessSchemaGenerator(business_data)
            html_code = generator.generate_html()
            
            st.success("✅ Schema generated!")
            st.code(html_code, language="html")
            
            st.download_button(
                "📥 Download HTML",
                html_code,
                file_name=f"{business_name.lower().replace(' ', '_')}_schema.html"
            )
else:
    st.warning("Add clients first.")
