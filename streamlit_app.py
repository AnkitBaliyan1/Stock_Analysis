import numpy as np
import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt


def main():
    # adding title to the page
    st.title("Stock Data Analysis")

    # information required for analysis
    user_input = st.text_area("Enter the Stock", 'AAPL')
    start = st.date_input("Enter start date")
    end = st.date_input("Enter the end date")

    # validating start and end date
    if start < end:
        st.success("Awesome Choice! Let's start the Analysis now.")
        st.subheader(f"Stock data from {start} - {end}")

        # check box to display moving average line
        # ma_state = st.checkbox("MA")
        # if ma_state:  # if user check the ma_state selecting time period is prompted
        # n = st.selectbox("Pick one", [50, 100, 200])

        st.write(" ")
        df = yf.download(user_input, start, end)  # downloading the data

        ls_col = list(df.columns)[0:5]  # pulling out columns names
        col = st.selectbox("Select Columns for Analysis", ls_col)  # giving user the option to select the column they want to perform analysis on

        # Plot 1, Trend Analysis
        fig = plt.figure(figsize=(12, 6))
        plt.plot(df[col], 'b', label='Stock price')  # plotting trend line

        ma_state = st.checkbox("MA")
        if ma_state:  # if user check the ma_state selecting time period is prompted
            n = st.selectbox("Pick one", [50, 100, 200])
            df_ma = df[col].rolling(n).mean()
            plt.plot(df_ma, 'r', label=f'MA{n}')  # plotting MA line

        plt.title(f"Trend Analysis for {user_input} ({col})")
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.legend()
        st.pyplot(fig)

        # Plot 2, Risk Analysis (%age change on daily basis)
        st.subheader("Risk and Volatility Analysis")
        df_pct = df[col].pct_change(periods=1)
        df_volatile = df[col].pct_change().rolling(30).std()
        fig = plt.figure(figsize=(12, 6))
        plt.plot(df_pct, 'y', label="%age change in price on daily basis")
        plt.plot(df_volatile, 'r', label='Volatility Pattern: SD over time')
        plt.title(f"Risk and Volatility Analysis for {user_input} - {col}")
        plt.legend()
        st.pyplot(fig)

        # Analysing Volume in Trade
        st.subheader("Volume in Trade")
        log_state = st.checkbox("Log scale")   # user to select the scale
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
