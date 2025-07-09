# app.py – FUndCell | End-to-End Fund Accounting Module for AMC
import streamlit as st
import pandas as pd
import plotly.express as px

# --- UI Setup ---
st.set_page_config(
    page_title="FundCell | AMC Fund Accounting",
    layout="wide"
)

st.markdown("""
    <style>
        body {background-color: #ffffff; color: #003366;}
        .stApp {background-color: #f9fbfc;}
    </style>
""", unsafe_allow_html=True)

# --- Sidebar Role Selector ---
st.sidebar.title("FundCell Login")
role = st.sidebar.selectbox("Select Your Role", [
    "Fund Accountant", "Fund Manager", "Compliance Officer", "Auditor", "Admin"
])

# --- Dashboard Logic ---
if role == "Fund Accountant":
    st.header("📘 Fund Accountant Dashboard")
    st.subheader("General Ledger Snapshot")
    st.dataframe(pd.DataFrame({
        "Account": ["Cash", "Receivables", "Payables", "Fixed Assets"],
        "Balance (₹ Cr)": [12.3, 3.2, -2.1, 5.7]
    }))

    st.subheader("NAV Status")
    navs = pd.DataFrame({
        "Fund": ["Blue Chip Equity", "Income Opportunities"],
        "NAV": [135.23, 102.75],
        "Status": ["Published", "Pending"]
    })
    st.dataframe(navs)

    st.subheader("Reconciliation Alerts")
    st.error("NAV mismatch in 'Income Opportunities'")

elif role == "Fund Manager":
    st.header("📊 Fund Manager Dashboard")
    st.subheader("Performance Analytics")
    perf_data = pd.DataFrame({
        "Metric": ["Sharpe Ratio", "Jensen’s Alpha", "Treynor Ratio"],
        "Value": [1.45, 2.1, 0.86]
    })
    st.dataframe(perf_data)

    st.subheader("Benchmarking")
    chart_data = pd.DataFrame({
        "Fund": ["Equity Fund", "Debt Fund", "Peer Avg"],
        "YTD Return %": [11.2, 6.3, 8.5]
    })
    st.bar_chart(chart_data.set_index("Fund"))

elif role == "Compliance Officer":
    st.header("🛡️ Compliance Officer Dashboard")
    st.subheader("Checklist")
    st.checkbox("✔ SEBI CTR Filed")
    st.checkbox("✔ FATCA/CRS Updated")
    st.checkbox("⚠ AML Alert: Pending Review")
    st.warning("2 STR transactions flagged")

    st.subheader("Regulatory Reporting")
    st.write("Portfolio Disclosures, Stress Tests, KYC/AML Filings")

elif role == "Auditor":
    st.header("🔍 Auditor Dashboard")
    st.subheader("Audit Trail Viewer")
    st.write("Showing all user actions in the past 30 days")
    st.download_button("Download Audit Logs", "User,Action,Timestamp\nadmin,Login,2025-07-09")

    st.subheader("Transaction Viewer")
    st.dataframe(pd.DataFrame({
        "Txn ID": [1001, 1002],
        "Fund": ["Blue Chip Equity", "Dynamic Bond"],
        "Amount": [1.2, 0.9],
        "Status": ["Approved", "Approved"]
    }))

elif role == "Admin":
    st.header("⚙️ Admin Dashboard")
    st.subheader("User Management")
    st.write("Active Users: 128 | New Registrations Today: 4")

    st.subheader("System Health")
    st.success("All integrations functional")
    st.info("Next backup scheduled at 2:00 AM IST")

    st.subheader("Security Logs")
    st.code("Unauthorized login attempt - user: guest")

# --- Footer ---
st.markdown("---")
st.caption("© 2025 FundCell by NAVIS | Secure. Automated. Compliant.")
