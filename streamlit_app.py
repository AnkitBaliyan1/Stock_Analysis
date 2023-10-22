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

    fig = plt.figure(figsize=(12, 6))
    plt.plot(df[col], 'b', label='Stock price')
    if ma_state:
        df_ma = df[col].rolling(n).mean()
        plt.plot(df_ma, 'r', label=f'MA{n}')
    plt.title(f"Stock: {user_input} ({col})")
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    st.pyplot(fig)

    log_state = st.checkbox("Log")
    st.subheader("Volume in Trade")
    fig2 = plt.figure(figsize=(12, 6))
    if log_state:
        plt.plot(np.log(df['Volume']), 'g', label='Volume Trade (log)')
    else:
        plt.plot(df['Volume'], 'g', label='Volume Trade')
    plt.legend()
    st.pyplot(fig2)

    st.subheader("               Thanks for giving it a shot..!!")


if __name__ == '__main__':
    main()
