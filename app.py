import streamlit as st
import pandas as pd

st.set_page_config(page_title='Aquarium Fertilizer Tracker', page_icon=':bar_chart:', layout='wide')

@st.cache_data
def load_data():
    return pd.read_csv('/app/data/aft.csv')

def main():
    st.title('Aquarium Fertilizer Tracker')
    data = load_data()
    st.dataframe(data)

if __name__ == '__main__':
    main()
