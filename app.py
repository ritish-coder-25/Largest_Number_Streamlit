# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import streamlit as st

# +
num1 = st.number_input("Enter First Number:")
num2 = st.number_input("Enter Second Number:")
num3 = st.number_input("Enter Third Number:")

largest = max(num1, num2, num3)

st.write("The Largest Number is: ", largest)
# -


