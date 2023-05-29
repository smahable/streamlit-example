from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import re

collect_numbers = lambda x : [int(i) for i in re.split("[^0-9]", x) if i != ""]

numbers = st.text_input("PLease enter numbers")
st.write(collect_numbers(numbers))

fixed_numbers = st.multiselect("Please select numbers", [1, 2, 3, 4, 5])
st.write(fixed_numbers)
"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


collect_numbers = lambda x : [int(i) for i in re.split("[^0-9]", x) if i != ""]

numbers = st.text_input("PLease enter numbers")
st.write(collect_numbers(numbers))

fixed_numbers = st.multiselect("Please select numbers", [1, 2, 3, 4, 5])
st.write(fixed_numbers)
