import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# --------------------
# PAGE CONFIG
# --------------------
st.set_page_config(
    page_title="VERDICT AI",
    page_icon="⚖️",
    layout="wide"
)

# --------------------
# CLEAN MODERN CSS - LIGHT THEME WITH PERFECT VISIBILITY
# --------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

/* Main Background - Clean White */
.stApp {
    background: #f8f9fa;
}

/* Smooth Animations */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes slideInRight {
    from {
        opacity: 0;
        transform: translateX(30px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

/* Hero Section */
.hero-section {
    text-align: center;
    padding: 3rem 2rem;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 20px;
    margin: 1rem 0 2rem 0;
    box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);
    animation: fadeInUp 0.8s ease-out;
}

.hero-title {
    font-size: 3.5rem;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 0.5rem;
    text-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.hero-subtitle {
    font-size: 1.5rem;
    color: #ffffff;
    font-weight: 400;
    margin-bottom: 0.5rem;
}

.hero-description {
    font-size: 1rem;
    color: #ffffff;
    opacity: 0.95;
    max-width: 700px;
    margin: 1rem auto;
}

/* Section Container */
.section-container {
    background: #ffffff;
    border-radius: 16px;
    padding: 2rem;
    margin: 1.5rem 0;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    border: 1px solid #e0e0e0;
    animation: fadeInUp 0.6s ease-out;
    transition: all 0.3s ease;
}

.section-container:hover {
    box-shadow: 0 8px 30px rgba(102, 126, 234, 0.15);
    transform: translateY(-2px);
}

/* Section Headers */
.section-header {
    font-size: 1.8rem;
    font-weight: 700;
    color: #1a1a1a;
    margin-bottom: 1.5rem;
    padding-bottom: 0.75rem;
    border-bottom: 3px solid;
    border-image: linear-gradient(90deg, #667eea, #764ba2) 1;
}

/* Metrics - High Contrast */
[data-testid="stMetricValue"] {
    font-size: 2rem !important;
    font-weight: 800 !important;
    color: #1a1a1a !important;
}

[data-testid="stMetricLabel"] {
    color: #4a5568 !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    font-size: 0.85rem !important;
}

[data-testid="stMetricDelta"] {
    color: #667eea !important;
    font-size: 0.9rem !important;
}

div[data-testid="metric-container"] {
    background: linear-gradient(145deg, #ffffff, #f8f9fa);
    padding: 1.5rem;
    border-radius: 12px;
    border: 2px solid #e0e0e0;
    transition: all 0.3s ease;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

div[data-testid="metric-container"]:hover {
    transform: translateY(-5px);
    border-color: #667eea;
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.2);
}

/* Chat Container */
.chat-container {
    background: #ffffff;
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1rem 0;
    border: 1px solid #e0e0e0;
    max-height: 500px;
    overflow-y: auto;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

/* Chat Messages - Perfect Visibility */
.user-message {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: #ffffff;
    padding: 1rem 1.5rem;
    border-radius: 18px 18px 4px 18px;
    margin: 0.75rem 0;
    margin-left: 20%;
    box-shadow: 0 3px 10px rgba(102, 126, 234, 0.3);
    font-size: 0.95rem;
    line-height: 1.6;
    animation: slideInRight 0.4s ease-out;
}

.ai-message {
    background: #f8f9fa;
    color: #1a1a1a;
    padding: 1rem 1.5rem;
    border-radius: 18px 18px 18px 4px;
    margin: 0.75rem 0;
    margin-right: 20%;
    border-left: 4px solid #667eea;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    font-size: 0.95rem;
    line-height: 1.6;
    animation: slideInRight 0.4s ease-out;
}

.ai-message strong {
    color: #667eea;
    font-weight: 700;
}

/* Buttons - High Visibility */
.stButton>button {
    background: linear-gradient(135deg, #667eea, #764ba2) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.7rem 1.8rem !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3) !important;
    font-size: 0.95rem !important;
}

.stButton>button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.5) !important;
}

/* Sidebar - Clean Light */
[data-testid="stSidebar"] {
    background: #ffffff !important;
    border-right: 1px solid #e0e0e0 !important;
}

[data-testid="stSidebar"] h2, 
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label {
    color: #1a1a1a !important;
}

/* File Uploader - Visible */
[data-testid="stFileUploader"] {
    background: #f8f9fa !important;
    border: 2px dashed #d0d0d0 !important;
    border-radius: 12px !important;
    padding: 1.5rem !important;
}

[data-testid="stFileUploader"]:hover {
    border-color: #667eea !important;
    background: #ffffff !important;
}

[data-testid="stFileUploader"] label,
[data-testid="stFileUploader"] section,
[data-testid="stFileUploader"] small {
    color: #1a1a1a !important;
}

/* Text Input - High Contrast */
.stTextInput>div>div>input {
    background: #ffffff !important;
    color: #1a1a1a !important;
    border: 2px solid #d0d0d0 !important;
    border-radius: 10px !important;
    padding: 0.75rem !important;
    font-size: 0.95rem !important;
}

.stTextInput>div>div>input:focus {
    border-color: #667eea !important;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
}

.stTextInput label {
    color: #1a1a1a !important;
    font-weight: 600 !important;
}

/* Alerts - Clear & Visible */
.stSuccess {
    background: #d4fce4 !important;
    color: #065f46 !important;
    border-left: 4px solid #10b981 !important;
    border-radius: 8px !important;
    padding: 1rem !important;
}

.stInfo {
    background: #dbeafe !important;
    color: #1e40af !important;
    border-left: 4px solid #3b82f6 !important;
    border-radius: 8px !important;
    padding: 1rem !important;
}

.stWarning {
    background: #fef3c7 !important;
    color: #92400e !important;
    border-left: 4px solid #f59e0b !important;
    border-radius: 8px !important;
    padding: 1rem !important;
}

.stError {
    background: #fee2e2 !important;
    color: #991b1b !important;
    border-left: 4px solid #ef4444 !important;
    border-radius: 8px !important;
    padding: 1rem !important;
}

/* Tabs - Clean Design */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background: #ffffff;
    padding: 0.5rem;
    border-radius: 10px;
    border: 1px solid #e0e0e0;
}

.stTabs [data-baseweb="tab"] {
    background: #f8f9fa;
    color: #4a5568;
    border-radius: 8px;
    padding: 0.7rem 1.5rem;
    font-weight: 600;
    border: 1px solid transparent;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #667eea, #764ba2) !important;
    color: #ffffff !important;
}

/* Download Button */
.stDownloadButton>button {
    background: linear-gradient(135deg, #10b981, #059669) !important;
    color: #ffffff !important;
}

.stDownloadButton>button:hover {
    background: linear-gradient(135deg, #059669, #047857) !important;
}

/* Badge */
.badge {
    display: inline-block;
    padding: 0.4rem 1rem;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 600;
    margin: 0.25rem;
}

.badge-success {
    background: linear-gradient(135deg, #10b981, #059669);
    color: #ffffff;
}

.badge-warning {
    background: linear-gradient(135deg, #f59e0b, #d97706);
    color: #ffffff;
}

.badge-info {
    background: linear-gradient(135deg, #3b82f6, #2563eb);
    color: #ffffff;
}

/* Info Card */
.info-card {
    background: #f8f9fa;
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1rem 0;
    border-left: 4px solid #667eea;
    border: 1px solid #e0e0e0;
}

.info-card h3 {
    color: #1a1a1a;
    margin-bottom: 0.75rem;
    font-weight: 700;
}

.info-card p {
    color: #4a5568;
    line-height: 1.6;
}

/* Product Row */
.product-row {
    padding: 1rem;
    margin: 0.5rem 0;
    background: #f8f9fa;
    border-radius: 8px;
    border: 1px solid #e0e0e0;
    transition: all 0.3s ease;
}

.product-row:hover {
    background: #ffffff;
    border-color: #667eea;
    transform: translateX(5px);
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 10px;
    height: 10px;
}

::-webkit-scrollbar-track {
    background: #f8f9fa;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(135deg, #667eea, #764ba2);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(135deg, #764ba2, #667eea);
}

/* Hide Streamlit Branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Ensure ALL text is dark and visible */
p, span, div, label, li {
    color: #1a1a1a !important;
}

h1, h2, h3, h4, h5, h6 {
    color: #1a1a1a !important;
}

/* Dataframe */
.dataframe {
    color: #1a1a1a !important;
}

</style>
""", unsafe_allow_html=True)

# --------------------
# INITIALIZE SESSION STATE
# --------------------
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'analysis_data' not in st.session_state:
    st.session_state.analysis_data = None
if 'uploaded_file_data' not in st.session_state:
    st.session_state.uploaded_file_data = None

# --------------------
# AI CHATBOT FUNCTION
# --------------------
def get_ai_response(user_query, analysis_data=None, uploaded_data=None):
    """Generate AI responses based on user queries and data context"""
    query_lower = user_query.lower()
    
    if analysis_data is not None:
        data = analysis_data
        
        if 'revenue' in query_lower or 'sales' in query_lower:
            total_revenue = data['revenue'].sum()
            best_product = data.loc[data['revenue'].idxmax(), 'product_id']
            return f"💰 **Revenue Insights:**\n\n- Total Revenue: **${total_revenue:,.0f}**\n- Best Performing Product: **Product {best_product}**\n- Average Revenue per Product: **${data['revenue'].mean():,.0f}**\n\n📊 Your sales data shows {'strong' if total_revenue > 5000 else 'moderate'} performance. Consider focusing marketing on Product {best_product}."
        
        elif 'profit' in query_lower or 'margin' in query_lower:
            total_profit = data['profit'].sum()
            avg_margin = data['margin'].mean()
            return f"📈 **Profitability Analysis:**\n\n- Total Profit: **${total_profit:,.0f}**\n- Average Margin: **{avg_margin:.1%}**\n- Status: **{'Healthy' if avg_margin > 0.25 else 'Needs Attention'}**\n\n{'✅ Your margins are solid! Consider scaling operations.' if avg_margin > 0.25 else '⚠️ Margins below optimal. Review pricing strategy or reduce costs.'}"
        
        elif 'improve' in query_lower or 'recommendation' in query_lower or 'suggest' in query_lower:
            avg_margin = data['margin'].mean()
            total_profit = data['profit'].sum()
            
            recommendations = "🎯 **Strategic Recommendations:**\n\n"
            
            if avg_margin < 0.25:
                recommendations += "1. **Pricing Optimization**: Increase prices 10-15% on high-demand products\n"
                recommendations += "2. **Cost Reduction**: Review supplier contracts and operational expenses\n"
            else:
                recommendations += "1. **Scale Marketing**: Your margins support increased ad spend\n"
                recommendations += "2. **Product Expansion**: Launch complementary products\n"
            
            if total_profit > 0:
                recommendations += "3. **Reinvestment**: Allocate 20% of profits to growth\n"
            else:
                recommendations += "3. **Urgent**: Implement cost-cutting measures immediately\n"
            
            return recommendations
        
        elif 'product' in query_lower and ('best' in query_lower or 'top' in query_lower):
            top_products = data.nlargest(3, 'profit')[['product_id', 'profit', 'margin']]
            response = "🏆 **Top Performing Products:**\n\n"
            for idx, row in top_products.iterrows():
                response += f"- **Product {row['product_id']}**: ${row['profit']:,.0f} profit ({row['margin']:.1%} margin)\n"
            return response
        
        elif 'risk' in query_lower or 'warning' in query_lower:
            total_profit = data['profit'].sum()
            low_margin_products = len(data[data['margin'] < 0.15])
            
            response = "⚠️ **Risk Assessment:**\n\n"
            if total_profit < 0:
                response += "🔴 **Critical**: Business operating at a loss\n"
                response += "- Immediate action required\n"
            elif low_margin_products > 0:
                response += f"🟡 **Moderate**: {low_margin_products} products below 15% margin\n"
                response += "- Consider repricing low-margin items\n"
            else:
                response += "🟢 **Low Risk**: All products performing well\n"
            
            return response
    
    if uploaded_data is not None:
        if 'summary' in query_lower or 'overview' in query_lower:
            return f"📊 **File Analysis:**\n\n- Rows: **{len(uploaded_data):,}**\n- Columns: **{len(uploaded_data.columns)}**\n- Fields: {', '.join(uploaded_data.columns.tolist())}"
    
    if 'help' in query_lower or 'what can you do' in query_lower:
        return """🤖 **I'm your AI Business Analyst!**

📊 **Data Analysis**: Upload data for instant insights
💡 **Recommendations**: Get strategies to improve
📈 **Performance**: Query revenue, profit, margins
⚠️ **Risk Assessment**: Identify issues
🎯 **Planning**: Get tailored advice

**Try asking:**
- "What's my total revenue?"
- "Which products should I focus on?"
- "How can I improve profitability?"
- "What are the risks?"
"""
    
    elif 'hello' in query_lower or 'hi' in query_lower:
        return "👋 Hello! I'm your AI business analyst. Upload your data and ask me anything!"
    
    else:
        return "🤔 Upload your files first, then ask about revenue, profit, recommendations, or products. Try 'What can you do?' to see all my capabilities."

# --------------------
# LOAD MOCK DATA
# --------------------
def load_mock_data():
    sales = pd.DataFrame({
        'product_id': [1, 2, 3, 4, 5],
        'price': [120, 80, 200, 150, 100],
        'units_sold': [15, 25, 10, 30, 20],
        'ad_spend': [50, 40, 70, 30, 20]
    })
    costs = pd.DataFrame({
        'product_id': [1, 2, 3, 4, 5],
        'cost_per_unit': [70, 50, 120, 90, 60]
    })
    customers = pd.DataFrame({
        'customer_id': [1, 2, 3, 4, 5, 6],
        'orders': [3, 1, 4, 2, 5, 3]
    })
    return sales, costs, customers

# --------------------
# HERO SECTION
# --------------------
st.markdown("""
<div class='hero-section'>
    <div class='hero-title'>⚖️ VERDICT AI</div>
    <div class='hero-subtitle'>Next-Generation Business Decision Engine</div>
    <div class='hero-description'>
        Transform your business data into actionable insights with AI-powered analytics
    </div>
</div>
""", unsafe_allow_html=True)

# --------------------
# SIDEBAR
# --------------------
st.sidebar.title("📂 Data Upload Center")

st.sidebar.subheader("📊 Core Business Data")
sales_file = st.sidebar.file_uploader("📈 Sales Data", type=["csv"], key="sales")
costs_file = st.sidebar.file_uploader("💰 Costs Data", type=["csv"], key="costs")
customers_file = st.sidebar.file_uploader("👥 Customers Data", type=["csv"], key="customers")

st.sidebar.markdown("---")

st.sidebar.subheader("🔍 Additional Analysis")
additional_file = st.sidebar.file_uploader("📎 Upload Any CSV", type=["csv"], key="additional")

st.sidebar.markdown("---")

st.sidebar.info("""
**💡 Pro Tips**

• Upload all files for complete analysis
• Use the chatbot for specific insights  
• Upload additional files for deep-dive
""")

# Process additional file
if additional_file is not None:
    st.session_state.uploaded_file_data = pd.read_csv(additional_file)
    st.sidebar.success(f"✅ Loaded: {additional_file.name}")
    st.sidebar.info(f"📊 {len(st.session_state.uploaded_file_data)} rows × {len(st.session_state.uploaded_file_data.columns)} columns")

# --------------------
# MAIN CONTENT - TABS
# --------------------
tab1, tab2 = st.tabs(["📊 Analytics Dashboard", "🤖 AI Assistant"])

# --------------------
# TAB 1: ANALYTICS DASHBOARD
# --------------------
with tab1:
    
    if st.button("🚀 Generate Full Report", type="primary", use_container_width=True):
        
        # Load data
        if sales_file and costs_file and customers_file:
            sales = pd.read_csv(sales_file)
            costs = pd.read_csv(costs_file)
            customers = pd.read_csv(customers_file)
            st.success("✅ Files loaded successfully!")
        else:
            sales, costs, customers = load_mock_data()
            st.info("ℹ️ Using demo data. Upload your files for real analysis.")

        # Process data
        data = sales.merge(costs, on="product_id")
        data["revenue"] = data["price"] * data["units_sold"]
        data["cost"] = data["cost_per_unit"] * data["units_sold"]
        data["profit"] = data["revenue"] - data["cost"] - data["ad_spend"]
        data["margin"] = data["profit"] / data["revenue"]
        
        st.session_state.analysis_data = data

        total_revenue = data["revenue"].sum()
        total_profit = data["profit"].sum()
        avg_margin = data["margin"].mean()
        avg_orders = customers["orders"].mean()

        # Executive Dashboard
        st.markdown("<div class='section-container'>", unsafe_allow_html=True)
        st.markdown("<h2 class='section-header'>📊 Executive Dashboard</h2>", unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Revenue", f"${total_revenue:,.0f}", delta="Revenue Stream")
        col2.metric("Total Profit", f"${total_profit:,.0f}", delta=f"{(total_profit/total_revenue)*100:.1f}%")
        col3.metric("Profit Margin", f"{avg_margin:.1%}", delta="Efficiency")
        col4.metric("Avg Orders", f"{avg_orders:.1f}", delta="Per Customer")
        
        st.markdown("</div>", unsafe_allow_html=True)

        # Charts
        st.markdown("<div class='section-container'>", unsafe_allow_html=True)
        st.markdown("<h2 class='section-header'>📈 Performance Analytics</h2>", unsafe_allow_html=True)
        
        viz_col1, viz_col2 = st.columns(2)
        
        with viz_col1:
            fig_revenue = px.bar(
                data, 
                x='product_id', 
                y='revenue',
                title="Revenue by Product",
                color='revenue',
                color_continuous_scale='Blues',
                labels={'product_id': 'Product ID', 'revenue': 'Revenue ($)'}
            )
            fig_revenue.update_layout(
                plot_bgcolor='white',
                paper_bgcolor='white',
                font=dict(color='#1a1a1a', family='Inter', size=12),
                title_font_size=16,
                title_font_color='#1a1a1a'
            )
            st.plotly_chart(fig_revenue, use_container_width=True)
        
        with viz_col2:
            fig_profit = px.bar(
                data,
                x='product_id',
                y='profit',
                title="Profit by Product",
                color='profit',
                color_continuous_scale='Purples',
                labels={'product_id': 'Product ID', 'profit': 'Profit ($)'}
            )
            fig_profit.update_layout(
                plot_bgcolor='white',
                paper_bgcolor='white',
                font=dict(color='#1a1a1a', family='Inter', size=12),
                title_font_size=16,
                title_font_color='#1a1a1a'
            )
            st.plotly_chart(fig_profit, use_container_width=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

        # AI Recommendations
        st.markdown("<div class='section-container'>", unsafe_allow_html=True)
        st.markdown("<h2 class='section-header'>🧠 AI Recommendations</h2>", unsafe_allow_html=True)
        
        rec_col1, rec_col2 = st.columns(2)
        
        with rec_col1:
            if avg_margin < 0.25:
                st.warning("🔴 **Pricing Alert**: Margins below 25%. Consider price optimization.")
                st.markdown("<span class='badge badge-warning'>Action Required</span>", unsafe_allow_html=True)
            else:
                st.success("🟢 **Pricing Status**: Healthy margins detected.")
                st.markdown("<span class='badge badge-success'>Optimal</span>", unsafe_allow_html=True)
        
        with rec_col2:
            if total_profit < 0:
                st.error("⚠️ **Risk Alert**: Operating at a loss!")
                st.markdown("<span class='badge badge-warning'>High Risk</span>", unsafe_allow_html=True)
            else:
                st.info("🟢 **Financial Health**: Business is profitable.")
                st.markdown("<span class='badge badge-success'>Stable</span>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

        # Customer Insights
        st.markdown("<div class='section-container'>", unsafe_allow_html=True)
        st.markdown("<h2 class='section-header'>👥 Customer Insights</h2>", unsafe_allow_html=True)
        
        fig_customers = px.histogram(
            customers,
            x='orders',
            nbins=10,
            title="Customer Orders Distribution",
            color_discrete_sequence=['#667eea'],
            labels={'orders': 'Number of Orders', 'count': 'Customer Count'}
        )
        fig_customers.update_layout(
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(color='#1a1a1a', family='Inter', size=12),
            title_font_size=16,
            title_font_color='#1a1a1a'
        )
        st.plotly_chart(fig_customers, use_container_width=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

        # Product Ranking
        st.markdown("<div class='section-container'>", unsafe_allow_html=True)
        st.markdown("<h2 class='section-header'>🏆 Top Products</h2>", unsafe_allow_html=True)
        
        top_products = data.nlargest(5, 'profit')[['product_id', 'revenue', 'profit', 'margin']]
        
        for idx, row in top_products.iterrows():
            st.markdown(f"""
            <div class='product-row'>
                <div style='display: flex; justify-content: space-between; align-items: center;'>
                    <div style='flex: 1;'>
                        <strong style='font-size: 1.1rem; color: #1a1a1a;'>Product {row['product_id']}</strong>
                    </div>
                    <div style='flex: 1; text-align: center; color: #4a5568;'>
                        Revenue: <strong style='color: #1a1a1a;'>${row['revenue']:,.0f}</strong>
                    </div>
                    <div style='flex: 1; text-align: center; color: #4a5568;'>
                        Profit: <strong style='color: #1a1a1a;'>${row['profit']:,.0f}</strong>
                    </div>
                    <div style='flex: 1; text-align: right;'>
                        <strong style='color: #667eea; font-size: 1.1rem;'>{row['margin']:.1%}</strong>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

        # Download
        st.download_button(
            "📥 Download Full Report",
            data=data.to_csv(index=False),
            file_name=f"verdict_ai_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
            use_container_width=True
        )

# --------------------
# TAB 2: AI CHATBOT
# --------------------
with tab2:
    
    st.markdown("<div class='section-container'>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-header'>🤖 AI Business Analyst</h2>", unsafe_allow_html=True)
    
    st.info("💬 Ask me anything about your business data and get instant insights!")
    
    # Chat Display
    st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
    
    if len(st.session_state.chat_history) == 0:
        st.markdown("""
        <div class='ai-message'>
            <strong>👋 Welcome!</strong><br><br>
            I'm your AI business analyst. Upload your files and ask questions like:<br>
            • "What's my total revenue?"<br>
            • "Which products are most profitable?"<br>
            • "Give me recommendations"<br>
            • "What are the risks?"
        </div>
        """, unsafe_allow_html=True)
    
    for message in st.session_state.chat_history:
        if message['role'] == 'user':
            st.markdown(f"<div class='user-message'>{message['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='ai-message'>{message['content']}</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Chat Input
    col1, col2 = st.columns([5, 1])
    
    with col1:
        user_input = st.text_input("Your question:", placeholder="e.g., What's my revenue?", label_visibility="collapsed")
    
    with col2:
        send_btn = st.button("Send 📤", use_container_width=True)
    
    if send_btn and user_input:
        st.session_state.chat_history.append({'role': 'user', 'content': user_input})
        ai_response = get_ai_response(user_input, st.session_state.analysis_data, st.session_state.uploaded_file_data)
        st.session_state.chat_history.append({'role': 'assistant', 'content': ai_response})
        st.rerun()
    
    # Quick Actions
    st.markdown("### 🎯 Quick Questions")
    
    quick_col1, quick_col2 = st.columns(2)
    
    with quick_col1:
        if st.button("💰 Revenue Analysis", use_container_width=True):
            st.session_state.chat_history.append({'role': 'user', 'content': 'What is my revenue?'})
            ai_response = get_ai_response('What is my revenue?', st.session_state.analysis_data, st.session_state.uploaded_file_data)
            st.session_state.chat_history.append({'role': 'assistant', 'content': ai_response})
            st.rerun()
        
        if st.button("💡 Get Recommendations", use_container_width=True):
            st.session_state.chat_history.append({'role': 'user', 'content': 'Give me recommendations'})
            ai_response = get_ai_response('Give me recommendations', st.session_state.analysis_data, st.session_state.uploaded_file_data)
            st.session_state.chat_history.append({'role': 'assistant', 'content': ai_response})
            st.rerun()
    
    with quick_col2:
        if st.button("📈 Profit Insights", use_container_width=True):
            st.session_state.chat_history.append({'role': 'user', 'content': 'Tell me about profit'})
            ai_response = get_ai_response('Tell me about profit', st.session_state.analysis_data, st.session_state.uploaded_file_data)
            st.session_state.chat_history.append({'role': 'assistant', 'content': ai_response})
            st.rerun()
        
        if st.button("⚠️ Risk Assessment", use_container_width=True):
            st.session_state.chat_history.append({'role': 'user', 'content': 'What are the risks?'})
            ai_response = get_ai_response('What are the risks?', st.session_state.analysis_data, st.session_state.uploaded_file_data)
            st.session_state.chat_history.append({'role': 'assistant', 'content': ai_response})
            st.rerun()
    
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)

# Additional File Analysis
if st.session_state.uploaded_file_data is not None:
    st.markdown("<div class='section-container'>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-header'>🔍 Additional File Analysis</h2>", unsafe_allow_html=True)
    
    uploaded_df = st.session_state.uploaded_file_data
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Rows", f"{len(uploaded_df):,}")
    col2.metric("Columns", len(uploaded_df.columns))
    col3.metric("Memory", f"{uploaded_df.memory_usage(deep=True).sum() / 1024:.1f} KB")
    
    st.subheader("📋 Data Preview")
    st.dataframe(uploaded_df.head(10), use_container_width=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 2rem;'>
    <h3 style='color: #667eea;'>Powered by VERDICT AI</h3>
    <p style='color: #4a5568;'>Making Data-Driven Decisions Effortless</p>
    <div style='margin-top: 1rem;'>
        <span class='badge badge-info'>Real-time Analytics</span>
        <span class='badge badge-success'>AI-Powered</span>
        <span class='badge badge-info'>Secure</span>
    </div>
</div>
""", unsafe_allow_html=True)