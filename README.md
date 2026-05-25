# Sales & Revenue Dashboard

A data visualization dashboard built with Python and Streamlit. Displays sales and revenue insights through interactive charts including KPI metrics, bar chart, line chart, pie chart, and a heatmap — all on a single page.

---

## Tech Stack

- **Python** — core language
- **Pandas** — data manipulation and aggregation
- **NumPy** — random data generation
- **Plotly Express** — interactive charts
- **Streamlit** — dashboard layout and web interface

---

## Features

- 4 KPI cards — Total Revenue, Total Units Sold, Best Product, Best Month
- Line chart — Revenue trend across months
- Bar chart — Revenue breakdown by product
- Pie chart — Units sold by region
- Heatmap — Revenue by product and month

---

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

**2. Install dependencies**

```bash
pip install pandas numpy plotly streamlit
```

**3. Run the dashboard**

```bash
streamlit run sales&revenue_dashboard.py
```

The dashboard will open automatically in your browser at `http://localhost:8501`

---

## Project Structure

```
├── sales&revenue_dashboard.py   # Main application file
└── README.md                    # Project documentation
```

---

## Data

This dashboard uses randomly generated fake sales data with the following structure:

| Column  | Description                          |
|---------|--------------------------------------|
| Date    | Random dates between 2025 and 2026   |
| Product | Laptop, Mobile, Headphones, Tablets  |
| Units   | Number of units sold (1–5)           |
| Region  | North, South, East, West             |
| Revenue | Calculated from product price × units|

Product prices used:
- Laptop — ₹80,000
- Mobile — ₹40,000
- Tablets — ₹60,000
- Headphones — ₹5,000

---

## How It Works

1. Fake sales data is generated on app load using NumPy and Pandas
2. KPI values are calculated using Pandas aggregations
3. Charts are built with Plotly Express using grouped data
4. Streamlit arranges everything into a single page layout

---

## Future Improvements

- [ ] Add date range filter to make charts interactive
- [ ] Connect to a real database instead of fake data
- [ ] Add a data table view below the charts
- [ ] Deploy to Streamlit Cloud for public access

---
