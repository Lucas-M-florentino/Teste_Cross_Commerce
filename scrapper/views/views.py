import pandas as pd
import json
import asyncio
from services.services import ScraperService
import streamlit as st
from streamlit_js_eval import streamlit_js_eval



def load_data():
    try:
        with open('database/numeros_ordenados.json', 'r') as f:
            numeros = pd.DataFrame(json.load(f), columns=["Numeros"])
        return numeros
    except FileNotFoundError:
        st.warning("Arquivo de números não encontrado.")
        return None 

def web_view():
    st.title("Visualização de Números Ordenados")
    
    numeros = load_data()
    
    if numeros is not None:
        st.write("Dados Carregados:")
        st.dataframe(numeros, use_container_width=True)
    else:
        if st.button("Capturar Dados"):
            scraper_service = ScraperService()
            asyncio.run(scraper_service.stream_paginas())
            st.success("Dados capturados e salvos com sucesso!")
            streamlit_js_eval(js_expressions="parent.window.location.reload()")
