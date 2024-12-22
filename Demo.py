import streamlit as st 
import json
import os
import pandas as pd

st.title('Forge Demo Datasets')
datasets = [f for f in os.listdir('dummy_data') if f != '.DS_Store']

vertical = st.selectbox('Select an app vertical', datasets, format_func=lambda x: x.replace('.csv', '').capitalize())

df = pd.read_csv('dummy_data/'+ vertical)
st.header(vertical.capitalize().replace('.csv', '') +  " dataset example (100k rows):")
st.write(df)

st.header("Strategies to explore")

with open('strategies/strategies.json', 'r') as f:
    strategies = json.load(f)
    strategy_points = strategies[vertical.replace('.csv','')]

def import_from(module, name):
    module = __import__(module, fromlist=[name])
    return getattr(module, name)

vertical_funcs = import_from('strategies.' + vertical.replace('.csv', ''), 'vertical_funcs')()

for func_name, func in vertical_funcs.items():
    st.subheader(func_name)
    st.info("Goal: "+  strategy_points[func_name])
    fig, explanation, reco = func(df)
    st.plotly_chart(fig)
    st.info(explanation)
    st.success(reco)
