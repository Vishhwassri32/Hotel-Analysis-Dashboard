# 🏨 Hotel Revenue & Booking Analytics Dashboard

An interactive hotel analytics project built to analyze **revenue performance, customer behavior, booking channels, room types, geographic markets, ratings, and cancellations**.

The project combines **Python, Pandas, Streamlit, Plotly, and Tableau** to transform raw hotel booking data into actionable business insights.

---

## 📊 Project Overview

The objective of this project is to understand the key drivers of hotel revenue and booking performance.

The analysis answers questions such as:

* Which countries generate the most revenue?
* Which room types contribute the most revenue?
* Which booking channels perform best?
* How does revenue change over time?
* Which countries generate the most guests?
* What is the cancellation rate?
* How do customer ratings vary across countries?
* What impact do payment status and promotions have on bookings?

---

## 🛠️ Tech Stack

| Technology          | Purpose                         |
| ------------------- | ------------------------------- |
| 🐍 Python           | Data cleaning and analysis      |
| 🐼 Pandas           | Data manipulation               |
| 📊 Plotly           | Interactive visualizations      |
| 🎨 Streamlit        | Interactive web dashboard       |
| 📈 Tableau          | Business intelligence dashboard |
| 📁 CSV              | Dataset storage                 |
| 📓 Jupyter Notebook | Exploratory Data Analysis       |

---

## 🚀 Dashboard Features

### 📌 Key Performance Indicators

* 💰 Total Revenue
* 🏨 Total Bookings
* 👥 Total Guests
* ⭐ Average Rating
* ❌ Cancellation Rate
* 🌙 Average Stay Duration

### 📊 Interactive Analysis

* Revenue by Booking Channel
* Revenue by Country
* Revenue by Room Type
* Monthly Revenue Trend
* Guests by Country
* Payment Status Analysis
* Cancellation Analysis
* Customer Rating Analysis
* Promotion Usage
* Stay Duration Analysis

### 🔎 Interactive Filters

Users can filter the dashboard by:

* Country
* Room Type
* Booking Channel
* Payment Status
* Promotion Usage
* Date

The charts update dynamically based on the selected filters.

---

## 💡 Key Business Insights

* 🇩🇪 **Germany generated the highest revenue** among the analyzed countries.
* 📞 **Phone bookings generated the highest revenue** among the booking channels.
* 🏨 **Suite rooms generated the highest revenue** among the room types.
* 💰 Total analyzed revenue was approximately **$75.58K**.
* 👥 The dataset contains approximately **460 guests across 150 bookings**.
* ❌ The overall cancellation rate was approximately **12.7%**.
* ⭐ The average customer rating was approximately **3.14/5**.
* 🌙 The average stay duration was approximately **3.9 days**.

---

## 📈 Tableau Dashboard

The project also includes a dedicated Tableau dashboard for business intelligence and visual analysis.

### Tableau Dashboard Preview

<img width="1636" height="994" alt="Hotel Analysis Dashboard" src="https://github.com/user-attachments/assets/64fa0a57-fa2a-4e9f-8ade-6719c841723d" />

---

## 🌐 Streamlit Application

A colorful and interactive **Streamlit + Plotly dashboard** provides additional exploration of the hotel booking data.

The application includes:

* Interactive KPI cards
* Dynamic filters
* Interactive Plotly charts
* Revenue analysis
* Customer analysis
* Booking-channel analysis
* Country-level analysis
* Cancellation analysis
* Business insights

### Run Locally

Clone the repository:

```bash
git clone https://github.com/Vishhwassri32/Hotel-Analysis-Dashboard.git
cd Hotel-Analysis-Dashboard
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```text
Hotel-Analysis-Dashboard/
│
├── app.py
├── requirements.txt
│
├── hotel_booking_data.csv
├── hotel_booking_cleaned.csv
│
├── hotel_analysis.ipynb
│
├── Hotel_Analysis_Dashboard.twb
│
├── Hotel-Analysis-Dashboard.png
│
├── README.md
└── analysis_visualizations/
```

---

## 🔄 Project Workflow

```text
Raw Hotel Booking Data
          ↓
    Data Cleaning
          ↓
   Exploratory Analysis
          ↓
   Feature Engineering
          ↓
 ┌────────┴─────────┐
 ↓                  ↓
Tableau          Streamlit
Dashboard        Application
 ↓                  ↓
 └────────┬─────────┘
          ↓
   Business Insights
```

---

## 🎯 Business Value

This project demonstrates how raw hotel booking data can be transformed into an interactive analytics solution that helps identify:

* High-performing markets
* Revenue-generating room types
* Strong booking channels
* Customer behavior patterns
* Cancellation trends
* Customer satisfaction patterns
* Revenue opportunities

---

## 👨‍💻 Author

**Vishwas Srivastava**

B.Tech Computer Science — Data Science

GitHub: [Vishwas Srivastava](https://github.com/Vishhwassri32)

LinkedIn: [Vishwas Srivastava](https://www.linkedin.com/in/srivastavavishwas/)

---

⭐ If you find this project useful, consider giving the repository a star!
