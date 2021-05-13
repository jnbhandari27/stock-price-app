import streamlit as st
import pandas as pd 
import yfinance as yf
from datetime import datetime 

st.write("""
# 🗠 Simple Stock Price App 🗠
### Get the data of top 50 stocks of USA in seconds! 🤩 
You can also calculate how rich the stock can make you! 🤑

Go to the sidebar to select the stock of your choice and the time period of the chart you want to view.

* To get the stock price chart as well as volume chart 📈 Click on **Show Chart**.

* To calculate returns from that stock 💲 Click on **Calculate Returns**.

""")
st.sidebar.header("Features")
now = datetime.date(datetime.now()) 
def user_input_features():
    tickerSymbol = st.sidebar.selectbox("Select the stock ticker:", ("AAPL","MSFT","AMZN","GOOG","FB", "BRK.A","TSLA","V","JPM","JNJ","WMT","UNH","MA","NVDA","HD","BAC","DIS","PG","PYPL","CMCSA","XOM","VZ","KO","ADBE","INTC","ORCL","T","CSCO","NFLX","PFE","NKE","CVX","ABT","ABBV","PEP","CRM","MRK","ACN","WFC","UPS","LLY","AVGO","DHR","TMO","MCD","TXN","MDT","COST","MS","HON"))
    selected_date = st.sidebar.text_input("Start date", "2010-01-01", key = 1)
    period = st.sidebar.selectbox("Select the timeframe:", ("1d", "1w", "1m"))
    return tickerSymbol, selected_date, period

def chart_plotter():
    st.line_chart(tickerDf.Close, use_container_width = True)
    st.bar_chart(tickerDf.Volume)

tickerSymbol, selected_date, period = user_input_features()  

tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period, start=selected_date, end= now)

if st.button("Show Chart"): 
    chart_plotter()

if st.button("Calculate Returns"):
    initial_investment = st.text_input("Enter initial investment in $","1000", key = 2)
    start_date = st.text_input("Start date", '2010-06-01',key = 3)
    initial_price =  tickerDf.loc[start_date]["Close"]
    number_of_stocks = int(initial_investment)/initial_price
    current_price = tickerDf["Close"].iloc[-1]
    current_investment = current_price*number_of_stocks
    difference = int(current_investment)-int(initial_investment)
    if difference > 0:
        result = "profit"
    else:
        result = "loss"
    st.write("Your",initial_investment,"$ invested in", tickerSymbol,"on", start_date,"would get you",number_of_stocks,"shares. \n These shares would now be worth", current_investment,"$, giving you a", result,"of", abs(difference),"$")
    
    