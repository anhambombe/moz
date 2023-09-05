import streamlit as st
import pandas as pd
import numpy as np
import openpyxl
#from openpyxl import load_workbook

import time

st.title("LQAS")
st.write("Dashboard do LQAS:")

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

DATE_COLUMN = 'Date_of_LQAS'
#@st.cache_data
lqas_url = "MOZ_SIA_LQAS_Assessment.xlsx"

data=pd.read_excel(lqas_url,
                 sheet_name="data")
hh_data=pd.read_excel(lqas_url,
                 sheet_name="Count_HH")


df = pd.merge(data, hh_data, left_on='_index', right_on='_parent_index', how='left')
option = st.selectbox(
    'Selecione a Ronda',
     df['Rnd'].unique())

'You selected: ', option

chart_data = df["Region"].value_counts()

st.line_chart(chart_data)



#map_data = df[['latitude','longitude']]

#st.map(map_data)
st.map(df,
    latitude='latitude',
    longitude='longitude',use_container_width=True
    )#size='col3',color='Vacinado'

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)
# Cria um DataFrame com a contagem de valores únicos na coluna "Vacinado"
resumo = pd.DataFrame(df["Vacinado"].value_counts())

# Renomeia a coluna para "Total"
resumo.columns = ["Total"]

# Escreve o DataFrame na tela
st.write(resumo)
