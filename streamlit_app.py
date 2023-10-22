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


if __name__ == '__main__':
    main()
