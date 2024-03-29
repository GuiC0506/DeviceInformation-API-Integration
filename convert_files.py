import pandas as pd
import streamlit as st
import os

def convert(df):
    return df.to_csv(index=False)

def get_extension(PATH):
    name, extension = os.path.splitext(PATH)
    return name, extension

st.cache_data()
def read_file(file):
    name, extension = get_extension(file.name)
    try:
        if extension in ('.xlsx', '.xls'):
            data = pd.read_excel(file)
        elif extension == '.csv':
            data = pd.read_csv(file)
        else:
            st.warning('Verifique se o arquivo possui extensão CSV, XLSX ou XLS.')
            data = None
        return data, extension, name
    except:
        st.warning('Verifique se o arquivo não está corrompido.')
        return None, None, None