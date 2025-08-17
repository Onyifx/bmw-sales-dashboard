import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("cleaned_bmw_car_sales_classification.csv")

# Page config
st.set_page_config(layout="wide", page_title="BMW Sales Dashboard")
st.title("🚗 BMW Sales Dashboard")
st.markdown("A visual overview of BMW's global sales performance with key insights.")

# Optional filters
st.sidebar.header("🔍 Filter Data")
years = st.sidebar.multiselect("Select Years", sorted(df['year'].unique()), default=sorted(df['year'].unique()))
regions = st.sidebar.multiselect("Select Regions", sorted(df['region'].unique()), default=sorted(df['region'].unique()))
filtered_df = df[df['year'].isin(years) & df['region'].isin(regions)]

# Chart 1: Sales Volume by Region
st.markdown("### 🌍 Sales Volume by Region")
col1, col2 = st.columns([2, 1])
with col1:
    region_sales = filtered_df.groupby('region')['sales_volume'].sum().sort_values(ascending=False).reset_index()
    fig1, ax1 = plt.subplots()
    sns.barplot(data=region_sales, x='region', y='sales_volume', palette='mako', ax=ax1)
    ax1.set_title("Top Performing Regions")
    ax1.set_xlabel("")
    ax1.set_ylabel("Sales Volume")
    plt.xticks(rotation=45)
    st.pyplot(fig1)
with col2:
    top_region = region_sales.iloc[0]
    st.subheader("📌 Insight")
    st.markdown(f"""
    - **{top_region['region']}** leads with **{top_region['sales_volume']:,} units sold**
    - Strong market presence and brand loyalty
    - Consider expanding dealership or marketing efforts in this region
    """)

# Chart 2: Sales Volume by Car Model
st.markdown("### 🚘 Sales Volume by Car Model")
col3, col4 = st.columns([2, 1])
with col3:
    model_sales = filtered_df.groupby('model')['sales_volume'].sum().sort_values(ascending=False).reset_index()
    fig2, ax2 = plt.subplots()
    sns.barplot(data=model_sales, x='model', y='sales_volume', palette='viridis', ax=ax2)
    ax2.set_title("Best-Selling Models")
    ax2.set_xlabel("")
    ax2.set_ylabel("Sales Volume")
    plt.xticks(rotation=45)
    st.pyplot(fig2)
with col4:
    top_model = model_sales.iloc[0]
    st.subheader("📌 Insight")
    st.markdown(f"""
    - **{top_model['model']}** is the top seller with **{top_model['sales_volume']:,} units**
    - Indicates strong consumer preference
    - Optimize production and promotion for this model
    """)

# Chart 3: Yearly Sales Trend
st.markdown("### 📈 Yearly Sales Trend")
col5, col6 = st.columns([2, 1])
with col5:
    yearly_sales = filtered_df.groupby('year')['sales_volume'].sum().reset_index()
    fig3, ax3 = plt.subplots()
    sns.lineplot(data=yearly_sales, x='year', y='sales_volume', marker='o', ax=ax3)
    ax3.set_title("Sales Over Time")
    ax3.set_ylabel("Sales Volume")
    st.pyplot(fig3)
with col6:
    growth = yearly_sales['sales_volume'].pct_change().fillna(0).mean()
    trend = "increasing" if growth > 0 else "declining"
    st.subheader("📌 Insight")
    st.markdown(f"""
    - Sales trend is **{trend}** with an average change of **{growth:.2%}**
    - Useful for forecasting and strategic planning
    - Investigate factors driving this trend
    """)

# Footer
st.markdown("---")
st.caption("Dashboard built with ❤️ using Streamlit, Seaborn, and Matplotlib.")
