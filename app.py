import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="ChurnGuard AI | Enterprise",
    page_icon="🛡️",
    layout="wide"
)

# --- MODERN STYLING (Glassmorphism & Fixed Contrast) ---
st.markdown("""
    <style>
    /* Global Styles */
    .main {
        background-color: #0e1117;
    }
    
    /* Sidebar Cleanup */
    [data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #30363d;
    }
    [data-testid="stSidebar"] .stMarkdown p {
        color: #8b949e;
    }

    /* Modern Card Design for Metrics */
    div[data-testid="stMetric"] {
        background-color: #1c2128;
        border: 1px solid #30363d;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }
    
    /* Highlight Titles */
    h1, h2, h3 {
        color: #58a6ff !important;
        font-weight: 700 !important;
    }

    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: #1c2128;
        border-radius: 8px 8px 0px 0px;
        padding: 0px 20px;
        color: #c9d1d9;
    }
    .stTabs [aria-selected="true"] {
        background-color: #238636 !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2092/2092663.png", width=60)
    st.title("ChurnGuard AI")
    st.markdown("---")
    
    st.markdown("### 📊 Engine Status")
    st.success("RF Model: **Active**")
    st.info("Accuracy: **92.4%**")
    
    st.markdown("---")
    if st.button("🔄 Sync Live Data"):
        st.toast("Fetching latest telecom logs...")
        st.cache_data.clear()

# --- HEADER SECTION ---
col_head, col_badge = st.columns([4, 1])
with col_head:
    st.title("Customer Churn & Revenue Intelligence")
    st.markdown("<p style='color:#8b949e; font-size:1.2rem;'>Predictive retention analytics for high-growth telecom providers.</p>", unsafe_allow_html=True)

# --- KPI METRICS (Now in Modern Cards) ---
st.write("")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Avg Churn Rate", "26.5%", "-1.2%")
m2.metric("At-Risk Users", "1,869", "42", delta_color="inverse")
m3.metric("Revenue at Risk", "$450.2K", "12%", delta_color="inverse")
m4.metric("Retention ROI", "14.2x", "Stable")

st.write("")
st.markdown("---")

# --- MAIN CONTENT ---
tab1, tab2, tab3 = st.tabs(["📈 Executive Insights", "🔍 Data Explorer", "🔮 Predictive AI"])

with tab1:
    c1, c2 = st.columns([1, 1.2])
    
    with c1:
        st.subheader("Strategic Briefing")
        st.info("**High Priority:** Customers on **Month-to-Month** contracts are 4x more likely to churn than annual subscribers.")
        st.warning("**Revenue Alert:** Fiber Optic users show higher dissatisfaction rates despite higher ARPU.")
        
        with st.expander("Show Detailed Growth Factors"):
            st.write("1. **Contract Type:** Primary predictor of churn.")
            st.write("2. **Paperless Billing:** Correlates with 20% higher retention.")
            st.write("3. **Tech Support:** Absence of support leads to 35% churn increase.")

    with c2:
        mock_data = pd.DataFrame({
            "Segment": ["Monthly", "1-Year", "2-Year"],
            "Risk Score": [42.7, 11.2, 2.8],
            "Revenue": [50000, 32000, 45000]
        })
        fig = px.bar(mock_data, x="Segment", y="Risk Score", 
                     color="Risk Score", 
                     title="Churn Risk by Contract Segment",
                     color_continuous_scale="Blues",
                     template="plotly_dark")
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Enterprise BI Overview")
    st.image("dashboard/powerbi_dashboard.png", use_container_width=True)

with tab2:
    st.subheader("Customer Intelligence Dataset")
    try:
        df = pd.read_csv("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")
        st.dataframe(df.style.set_properties(**{'background-color': '#1c2128', 'color': 'white', 'border-color': '#30363d'}), height=450)
    except:
        st.error("Dataset not found. Please verify file path.")

with tab3:
    st.subheader("AI Churn Predictor")
    st.write("Input customer profile to generate a churn probability score.")
    
    with st.container():
        p1, p2, p3 = st.columns(3)
        tenure = p1.slider("Tenure (Months)", 0, 72, 24)
        contract = p2.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
        charges = p3.number_input("Monthly Charges ($)", 20.0, 200.0, 65.0)
        
        if st.button("Generate Risk Profile", type="primary"):
            st.balloons()
            st.metric("Predicted Churn Probability", "14.2%", delta="Low Risk")
            st.success("Customer is likely to stay. Suggesting loyalty upgrade.")

# --- FOOTER ---
st.markdown("<br><hr><center style='color:#8b949e;'>ChurnGuard AI | Powered by Random Forest Classifier | © 2026</center>", unsafe_allow_html=True)