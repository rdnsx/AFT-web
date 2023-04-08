import streamlit as st
import pandas as pd

st.set_page_config(page_title='My CSV Viewer', page_icon=':bar_chart:', layout='wide')

@st.cache
def load_data():
    return pd.read_csv('/app/data/data.csv')

def main():
    st.title('My CSV Viewer')
    data = load_data()
    st.dataframe(data)

if __name__ == '__main__':
    main()
