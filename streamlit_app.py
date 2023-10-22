import pandas as pd
import numpy as np
import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# user_input = 'AAPL'
start = '2010-01-01'
end = '2023-01-01'
col = 'Adj Close'
# n = 100


def main():
    st.title("Stock Data Analysis")
    st.subheader(f"Stock data from {start} - {end}")

    user_input = st.text_area("Enter the Stock", 'AAPL')

    ma_state = st.checkbox("MA")
    if ma_state:
        n = st.selectbox("Pick one", [50, 100, 200])

    st.write(" ")
    # if st.button("Submit"):
    df = yf.download(user_input, start, end)
    # print(df.head())
    st.write("all good here.")

if __name__ == '__main__':
    main()
