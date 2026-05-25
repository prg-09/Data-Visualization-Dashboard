import pandas as pd
import plotly.express as px
import numpy as np
import streamlit as st


def date():
    dp = pd.date_range(start= '2025-01-01' , end= '2026-01-01', freq= 'D')
    date_chosen = pd.to_datetime(np.random.choice(dp, size=50))
    return date_chosen

def product ():
    product = ["Laptop","Mobile","Headphones","Tablets" ]
    priorities = [0.1,0.3,0.4,0.2]
    product_chosen = np.random.choice(product, size = 50, p = priorities)
    # print  (product_chosen)
    return product_chosen

def units():
    units = [1,2,3,4,5]
    units_chosen = np.random.choice(units, size = 50)
    # print (units_chosen)
    return units_chosen

def region():
    region = [ "North","South","East","West"]
    priorities = [0.2,0.3,0.4,0.1]
    region_chosen = np.random.choice(region, size = 50, p=priorities)
    # print (region_chosen)
    return region_chosen

def revenue (product_chosen, unit_chosen):
    prices = {
        "Laptop": 80000,
        "Mobile": 40000,
        "Headphones": 5000,
        "Tablets": 60000
    }
    series = pd.Series(product_chosen)
    price = series.map(prices)
    revenue = price * unit_chosen
    # print(revenue)
    return revenue

def build_dataset():
    dates    = date()
    products = product()
    unit_qty = units()
    regions  = region()
    rev      = revenue(products, unit_qty) 

    df = pd.DataFrame({
        "Date" : dates,
        "Product": products,
        "Units": unit_qty,
        "Region": regions,
        "Revenue": rev
    })
    # print (df)
    return df
dataset = build_dataset()


total_revenue = dataset["Revenue"].sum()
total_units = dataset["Units"].sum()
best_product = dataset.groupby("Product")["Revenue"].sum().idxmax()
best_month = dataset.groupby(dataset["Date"].dt.month)["Revenue"].sum().idxmax()



month = {
    1 : "Jan",
    2 : "Feb",
    3:"Mar",
    4:"Apr",
    5:"May",
    6:"Jun",
    7:"Jul",
    8:"Aug",
    9:"Sept",
    10:"Oct",
    11:"Nov",
    12:"Dec"
    
}



col1, col2, col3, col4 = st.columns(4)
with col1: 
    st.metric(label = 'Total Revenue', value = total_revenue)

with col2:
    st.metric(label = 'Total Units', value = total_units)
with col3:
    st.metric(label = 'Best Product', value = best_product)
with col4:
    st.metric(label = 'Best Month', value = month[best_month])
    
    
revenue_by_product = dataset.groupby("Product")["Revenue"].sum().reset_index()
bar = px.bar(revenue_by_product, x="Product", y="Revenue", title="Revenue by Product", color="Product")
st.plotly_chart(bar) 
  
revenue_by_month = dataset.groupby(dataset["Date"].dt.month)["Revenue"].sum().reset_index()
revenue_by_month.columns = ["Month", "Revenue"]
line = px.line(revenue_by_month, x="Month", y="Revenue", title="Revenue by Month", markers=True)
st.plotly_chart(line) 

pie = px.pie(dataset,names = "Region", values = "Units", title = "Pie Chart showing units sold by Region")
st.plotly_chart(pie) 

heatmap = px.density_heatmap(dataset, x="Product", y=dataset["Date"].dt.month, z="Revenue", histfunc="sum", title="Revenue Heatmap by Product & Month")
st.plotly_chart(heatmap) 
