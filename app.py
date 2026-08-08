import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="Hotel Revenue Analytics",
    page_icon="🏨",
    layout="wide"
)

st.title("🏨 Hotel Revenue & Booking Analytics")

df = pd.read_csv("hotel_booking_data.csv")

# KPIs
total_revenue = df["TotalAmount"].sum()
total_bookings = len(df)
total_guests = df["Guests"].sum()
avg_rating = df["Rating"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Bookings", total_bookings)
col3.metric("Guests", total_guests)
col4.metric("Avg Rating", f"{avg_rating:.2f}")

st.divider()

st.subheader("Revenue by Room Type")

revenue_room = (
    df.groupby("RoomType")["TotalAmount"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(revenue_room)

st.subheader("Revenue by Booking Channel")

revenue_channel = (
    df.groupby("BookingChannel")["TotalAmount"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(revenue_channel)

st.subheader("Revenue by Country")

revenue_country = (
    df.groupby("Country")["TotalAmount"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(revenue_country)