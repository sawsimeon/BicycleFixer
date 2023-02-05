import streamlit as st
import pandas as pd
import numpy as np

st.title('Latest bicycle map!')

st.write("Look no further than the latest bicycle map! We have compiled the latest information on bicycle availability at local stores in Uppsala and surrounding areas. With this map, you can easily find bicycles that are available and spot any deals that might be available.")

st.write("The map also shows information about the types of bikes available. We are constantly updating our map to reflect the current availability of bicycles. So if you're looking for a bike to ride, make sure to check out our bicycle map. We make it easy and convenient to find the best bicycle for you, no matter where you are located.")

df = pd.DataFrame({"lat": [59.842862, 59.85640589725369, 59.85343109342867],
                   "lon": [17.637734, 17.611705669934945, 17.63566915158178]})

st.map(df)