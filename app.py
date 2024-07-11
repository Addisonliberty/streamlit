import pandas as pd
import numpy as np
import streamlit as st

st.title("Trying this Out")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.table(chart_data)

st.checkbox("I like the table")

st.line_chart(chart_data)