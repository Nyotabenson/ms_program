import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



data = {'uni' : ['msu', 'uof', 'qui'],
        'BA' : [3.0, 2.9, 3.1],
         'DS' : [3.12, 3.5, 3.6] }

df = pd.DataFrame(data)

st.dataframe(df)




plt.bar(df.uni, df.BA)
st.pyplot(plt)