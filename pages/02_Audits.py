import streamlit as st
from utils.audit_tool import run_audit
import pandas as pd

st.title("🔍 Run AI Visibility Audit")

# Client selector
if st.session_state.clients:
    client_names = [c['business_name'] for c in st.session_state.clients]
    selected = st.selectbox("Select Client", client_names)
    
    # Find selected client
    client = next(c for c in st.session_state.clients if c['business_name'] == selected)
    
    st.markdown(f"**Website:** {client['website']}")
    
    if st.button("🚀 Run Audit", type="primary"):
        with st.spinner("Analyzing website..."):
            # Call your audit tool
            results = run_audit(client['website'])
            
            # Store results in session state
            if 'audit_results' not in st.session_state:
                st.session_state.audit_results = []
            
            audit_record = {
                "client": client['business_name'],
                "date": pd.Timestamp.now(),
                "score": results['score'],
                "schema_found": results['schema_found'],
                "entities_found": results['entities_found'],
                "recommendations": results['recommendations']
            }
            st.session_state.audit_results.append(audit_record)
            
            # Display results
            st.success("Audit complete!")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("AI Visibility Score", f"{results['score']}/100")
            with col2:
                st.metric("Schema Detected", "✅" if results['schema_found'] else "❌")
            
            st.subheader("📋 Recommendations")
            for rec in results['recommendations']:
                st.write(f"• {rec}")
            
            # Offer to fix
            if st.button("🛠️ Fix These Issues", type="primary"):
                st.switch_page("pages/03_Schema_Fixer.py")
else:
    st.warning("Add clients first before running audits.")
