import streamlit as st
import pandas as pd
import numpy as np
import time

st.title('Safe boda pickups in Kampala')

DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

