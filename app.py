import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ==========================================
# 1. PAGE CONFIGURATION & STYLING
# ==========================================
st.set_page_config(
    page_title="Hotel Revenue & Booking Analytics",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Modern Dark/Gradient Dashboard UI & KPI Cards
st.markdown("""
    <style>
    /* Main background and font styling */
    .main {
        background-color: #0e1117;
        color: #fafafa;
    }
    /* Custom KPI Metric Cards */
    div.metric-card {
        background: linear-gradient(135deg, #1f2937 0%, #111827 100%);
        border: 1px solid #374151;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. DATA LOADING & PREPARATION
# ==========================================
@st.cache_data
def load_data():
    # Update path to match your actual file name
    df = pd.read_csv("hotel_booking_cleaned.csv")
    
    # Ensure date columns are parsed properly if available
    date_columns = [col for col in df.columns if 'date' in col.lower() or 'time' in col.lower()]
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')
        
    return df

try:
    df_raw = load_data()
except Exception as e:
    st.error(f"Error loading data: {e}. Please ensure 'data/hotel_booking_cleaned.csv' exists.")
    st.stop()

# ==========================================
# 3. SIDEBAR FILTERS
# ==========================================
st.sidebar.markdown("## 🔎 Dashboard Filters")
st.sidebar.markdown("Customize your view across dimensions.")

# Reset or Filter options
with st.sidebar.expander("Filter Controls", expanded=True):
    # Country Filter
    countries = sorted(df_raw["Country"].dropna().unique()) if "Country" in df_raw.columns else []
    selected_countries = st.multiselect("Select Country/Countries", countries, default=countries)

    # Room Type Filter
    room_types = sorted(df_raw["RoomType"].dropna().unique()) if "RoomType" in df_raw.columns else []
    selected_rooms = st.multiselect("Select Room Type(s)", room_types, default=room_types)

    # Booking Channel Filter
    channels = sorted(df_raw["BookingChannel"].dropna().unique()) if "BookingChannel" in df_raw.columns else []
    selected_channels = st.multiselect("Select Booking Channel(s)", channels, default=channels)

# Apply Filters
df = df_raw.copy()
if selected_countries and "Country" in df.columns:
    df = df[df["Country"].isin(selected_countries)]
if selected_rooms and "RoomType" in df.columns:
    df = df[df["RoomType"].isin(selected_rooms)]
if selected_channels and "BookingChannel" in df.columns:
    df = df[df["BookingChannel"].isin(selected_channels)]
# ==========================================
# 4. MAIN HEADER & TOP-LEVEL KPIS
# ==========================================
st.title("🏨 Hotel Revenue & Booking Analytics Dashboard")
st.markdown("Comprehensive overview of property performance, guest behaviors, revenue trends, and operational bottlenecks.")

# Compute Core KPIs
total_revenue = df["TotalAmount"].sum() if "TotalAmount" in df.columns else 0
total_bookings = len(df)
total_guests = df["Guests"].sum() if "Guests" in df.columns else 0
avg_rating = df["Rating"].mean() if "Rating" in df.columns else 0
cancellation_rate = (df["IsCanceled"].mean() * 100) if "IsCanceled" in df.columns else 0

# Render KPI Metric Cards
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Total Bookings", f"{total_bookings:,}")
col3.metric("Total Guests", f"{total_guests:,}")
col4.metric("Avg Guest Rating", f"{avg_rating:.2f} ⭐")
col5.metric("Cancellation Rate", f"{cancellation_rate:.1f}%")

st.divider()

# ==========================================
# 5. AUTOMATED BUSINESS INSIGHTS
# ==========================================
st.subheader("💡 Automated Business Insights")
col_insight1, col_insight2 = st.columns(2)

with col_insight1:
    top_room = df.groupby("RoomType")["TotalAmount"].sum().idxmax() if "RoomType" in df.columns and not df.empty else "N/A"
    st.info(f"🔥 **Top Revenue Generator:** Room Type **{top_room}** brings in the highest aggregate income across the selected parameters.")

with col_insight2:
    top_channel = df.groupby("BookingChannel")["TotalAmount"].sum().idxmax() if "BookingChannel" in df.columns and not df.empty else "N/A"
    st.success(f"🚀 **Primary Acquisition Channel:** **{top_channel}** is driving the most conversions and total volume.")

st.divider()

# ==========================================
# 6. INTERACTIVE PLOTLY CHARTS (6-10 CHARTS)
# ==========================================
color_theme = "Sunsetdark"

# Row 1: Room Type & Booking Channel Analysis
r1_col1, r1_col2 = st.columns(2)

with r1_col1:
    st.subheader("🏨 Revenue by Room Type")
    if "RoomType" in df.columns and "TotalAmount" in df.columns:
        fig_room = px.bar(
            df.groupby("RoomType", as_index=False)["TotalAmount"].sum().sort_values(by="TotalAmount", ascending=False),
            x="RoomType", y="TotalAmount", text_auto=".2s", color="TotalAmount",
            color_continuous_scale="Viridis"
        )
        fig_room.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_room, use_container_width=True)

with r1_col2:
    st.subheader("📱 Revenue by Booking Channel")
    if "BookingChannel" in df.columns and "TotalAmount" in df.columns:
        fig_channel = px.pie(
            df.groupby("BookingChannel", as_index=False)["TotalAmount"].sum(),
            names="BookingChannel", values="TotalAmount", hole=0.4,
            color_discrete_sequence=px.colors.sequential.Plasma
        )
        fig_channel.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_channel, use_container_width=True)

# Row 2: Monthly Trend & Cancellation Analysis
r2_col1, r2_col2 = st.columns(2)

with r2_col1:
    st.subheader("📅 Monthly Revenue Trend")
    date_col = next((col for col in ["CheckInDate", "BookingDate", "Date"] if col in df.columns), None)
    if date_col and not df.empty:
        df["YearMonth"] = df[date_col].dt.to_period("M").astype(str)
        monthly_trend = df.groupby("YearMonth", as_index=False)["TotalAmount"].sum()
        fig_trend = px.line(
            monthly_trend, x="YearMonth", y="TotalAmount", markers=True,
            line_shape="spline", color_discrete_sequence=["#00CC96"]
        )
        fig_trend.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_trend, use_container_width=True)
    else:
        st.warning("Date-based column not detected for trend mapping.")

with r2_col2:
    st.subheader("❌ Cancellation Analysis by Channel")
    if "BookingChannel" in df.columns and "IsCanceled" in df.columns:
        cancel_df = df.groupby("BookingChannel", as_index=False)["IsCanceled"].mean()
        cancel_df["IsCanceled"] = cancel_df["IsCanceled"] * 100
        fig_cancel = px.bar(
            cancel_df, x="BookingChannel", y="IsCanceled", text_auto=".1f",
            color="IsCanceled", color_continuous_scale="Reds"
        )
        fig_cancel.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_cancel, use_container_width=True)

# Row 3: Country Map / Geo Distribution & Rating Analysis
r3_col1, r3_col2 = st.columns(2)

with r3_col1:
    st.subheader("🌍 Top Countries by Revenue")
    if "Country" in df.columns and "TotalAmount" in df.columns:
        country_df = df.groupby("Country", as_index=False)["TotalAmount"].sum().nlargest(10, "TotalAmount")
        fig_country = px.bar(
            country_df, x="TotalAmount", y="Country", orientation="h",
            color="TotalAmount", color_continuous_scale="Tealgrn"
        )
        fig_country.update_layout(template="plotly_dark", yaxis={'categoryorder':'total ascending'}, plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_country, use_container_width=True)

with r3_col2:
    st.subheader("⭐ Guest Ratings Distribution")
    if "Rating" in df.columns:
        fig_rating = px.histogram(
            df, x="Rating", nbins=10, color_discrete_sequence=["#AB63FA"],
            marginal="box"
        )
        fig_rating.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_rating, use_container_width=True)

# Row 4: Promo Code & Payment Status Analytics
r4_col1, r4_col2 = st.columns(2)

with r4_col1:
    st.subheader("🎟️ Promo Code Impact on Bookings")
    promo_col = next((col for col in ["PromoCode", "HasPromo", "Discount"] if col in df.columns), None)
    if promo_col:
        promo_df = df.groupby(promo_col, as_index=False)["TotalAmount"].sum()
        fig_promo = px.pie(
            promo_df, names=promo_col, values="TotalAmount",
            color_discrete_sequence=px.colors.sequential.RdBu
        )
        fig_promo.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_promo, use_container_width=True)
    else:
        st.info("Promo code dimension field not present in current schema.")

with r4_col2:
    st.subheader("💳 Payment Status Breakdown")
    pay_col = next((col for col in ["PaymentStatus", "PaymentType"] if col in df.columns), None)
    if pay_col:
        pay_df = df.groupby(pay_col, as_index=False).size()
        fig_pay = px.bar(
            pay_df, x=pay_col, y="size", text_auto=True,
            color=pay_col, color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig_pay.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_pay, use_container_width=True)
    else:
        st.info("Payment status column not detected in current schema.")

st.divider()

# ==========================================
# 7. FILTERED DATA TABLE VIEW
# ==========================================
st.subheader("📋 Detailed Filtered Dataset Explorer")
with st.expander("Click to view and export raw data rows based on current filters", expanded=False):
    st.dataframe(df, use_container_width=True)
    
    # Download button for filtered dataset
    csv_data = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Filtered Data as CSV",
        data=csv_data,
        file_name="filtered_hotel_revenue_data.csv",
        mime="text/csv"
    )