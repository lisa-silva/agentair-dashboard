import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Analytics & Reports")

if 'audit_results' in st.session_state and st.session_state.audit_results:
    df = pd.DataFrame(st.session_state.audit_results)
    
    # Score trend
    fig = px.line(df, x='date', y='score', title='Audit Scores Over Time')
    st.plotly_chart(fig, use_container_width=True)
    
    # Recent audits
    st.subheader("Recent Audits")
    st.dataframe(df[['client', 'date', 'score']])
    
    # Export
    csv = df.to_csv(index=False)
    st.download_button(
        "📥 Download Report CSV",
        csv,
        file_name="agentair_reports.csv"
    )
else:
    st.info("Run some audits first to see reports.")
