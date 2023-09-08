from streamlit_gsheets import GSheetsConnection
import streamlit as st 

url = "https://docs.google.com/spreadsheets/d/118AeMVlvvmBsFmgv4FxURnZEs2pn_nKRGZqgniMaf2c/edit?usp=sharing"

conn = st.experimental_connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, col=[0,1])

st.dataframe(data)
