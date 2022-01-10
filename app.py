import pandas as pd
import datetime
import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt


st.markdown('''
# Historical stock prices 

''')
st.write('---')


st.sidebar.subheader('User input')
tickers = pd.read_csv('tickers.csv') 
sym = st.sidebar.selectbox('Choose the ticker here', tickers)
start_date = st.sidebar.date_input("Start date", datetime.date(2021, 12, 1))
end_date = st.sidebar.date_input("End date", datetime.date(2022, 1, 1))



Data = yf.Ticker(sym) 
tickerDataFrame = Data.history(period='1d', start= start_date, end= end_date)


st.header('**Ticker data**')
st.write(tickerDataFrame)



st.set_option('deprecation.showPyplotGlobalUse', False)
df = pd.DataFrame(tickerDataFrame.Close)
df['Date'] = df.index
plt.fill_between(df.Date, df.Close, color='red', alpha=0.5)
plt.plot(df.Date, df.Close, color='blue', alpha=0.5)
plt.xticks(rotation=90)
plt.title(sym, fontweight='bold')
plt.xlabel('Date', fontweight='bold')
plt.ylabel('Closing Price', fontweight='bold')
st.pyplot()
