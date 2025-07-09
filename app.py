# app.py – Simplified FundCell | AMC Fund Accounting Prototype
import streamlit as st
import pandas as pd

# --- UI Setup ---
st.set_page_config(
    page_title="FundCell | AMC Fund Accounting",
    layout="wide"
)

# --- Sidebar Role Selector ---
st.sidebar.title("FundCell Login")
role = st.sidebar.radio("Select Role", [
    "Fund Accountant", "Fund Manager", "Compliance Officer", "Auditor", "Admin"
])

# --- Role Dashboards ---
if role == "Fund Accountant":
    st.title("Fund Accountant Dashboard")
    st.write("### General Ledger Snapshot")
    st.dataframe(pd.DataFrame({
        "Account": ["Cash", "Receivables", "Payables", "Assets"],
        "Balance (₹ Cr)": [12.3, 3.2, -2.1, 5.7]
    }))
    st.write("### NAV Status")
    st.dataframe(pd.DataFrame({
        "Fund": ["Blue Chip", "Growth Fund"],
        "NAV": [135.23, 102.75],
        "Status": ["Published", "Pending"]
    }))

elif role == "Fund Manager":
    st.title("Fund Manager Dashboard")
    st.write("### Performance Metrics")
    st.dataframe(pd.DataFrame({
        "Metric": ["Sharpe", "Alpha", "Treynor"],
        "Value": [1.4, 2.1, 0.86]
    }))
    st.write("### Benchmarking")
    st.bar_chart(pd.DataFrame({
        "YTD Return %": [11.2, 6.3, 8.5]
    }, index=["Equity Fund", "Debt Fund", "Peer Avg"]))

elif role == "Compliance Officer":
    st.title("Compliance Officer Dashboard")
    st.write("### Compliance Checklist")
    st.checkbox("SEBI Report Filed")
    st.checkbox("AML Review Complete")
    st.warning("2 Suspicious Transactions Pending Review")

elif role == "Auditor":
    st.title("Auditor Dashboard")
    st.write("### Audit Logs")
    st.download_button("Download Logs", "User,Action,Time\nadmin,Login,2025-07-09")
    st.write("### Transactions")
    st.dataframe(pd.DataFrame({
        "Txn ID": [1001, 1002],
        "Amount": [1.2, 0.9],
        "Status": ["Approved", "Approved"]
    }))

elif role == "Admin":
    st.title("Admin Dashboard")
    st.write("### User Management")
    st.write("128 Active | 4 New Today")
    st.write("### System Health")
    st.success("All systems operational")

# --- Footer ---
st.markdown("---")
st.caption("© 2025 FundCell by NAVIS")
