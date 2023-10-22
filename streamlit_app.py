import pandas as pd
import numpy as np
import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

def main():
    # adding title to the page
    st.title("Stock Data Analysis")

    user_input = st.text_area("Enter the Stock", 'AAPL')
    start = st.date_input("Enter start date")
    end = st.date_input("Enter the end date")

    if start < end:
        st.success("Awesome Choice! Let's start the Analysis now.")
        st.subheader(f"Stock data from {start} - {end}")

        ma_state = st.checkbox("MA")
        if ma_state:
            n = st.selectbox("Pick one", [50, 100, 200])

        st.write(" ")
        # if st.button("Submit"):
        df = yf.download(user_input, start, end)
        # print(df.head())

        ls_col = list(df.columns)[0:5]
        col = st.selectbox("Select Columns for Analysis", ls_col)
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

        st.subheader("Percentage Change")
        dfpct = df[col].pct_change(periods=1)
        fig = plt.figure(figsize=(12, 6))
        plt.plot(dfpct, 'b')
        plt.title(f"%age change in {col}")
        st.pyplot(fig)

        st.subheader("Volume in Trade")
        log_state = st.checkbox("Log scale")
        fig = plt.figure(figsize=(12, 6))
        if log_state:
            plt.plot(np.log(df['Volume']), 'g', label='Volume Trade (log)')
        else:
            plt.plot(df['Volume'], 'g', label='Volume Trade')
        plt.legend()
        st.pyplot(fig)

        st.write("all done")
    elif start == end:
        st.warning("Start date is the same as the end date.")
    else:
        st.error("Start date is after the end date.")


if __name__ == '__main__':
    main()
