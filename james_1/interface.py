import streamlit as st
import json

with open('./Estatísticas Padrão.json', 'r') as arquivo_json:
    data_lida = json.load(arquivo_json)

# Imprimindo os dados lidos
st.write(data_lida)