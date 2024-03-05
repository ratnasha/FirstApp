import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dummy-Daten für die Bevölkerungsstatistik von Bern der letzten 10 Jahre
data = {
    'Jahr': [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Bevoelkerung': [128148, 129619, 131273, 132910, 134504, 135920, 137685, 139059, 140634, 141854, 142517, 143187]
}

df = pd.DataFrame(data)

# Titel der App
st.title('Bevölkerungsstatistik von Bern')

# Textelement
st.header('Übersicht')
st.write('Diese App zeigt das Bevölkerungswachstum von Bern der letzten 10 Jahre.')

# Datalemente
st.subheader('Datentabelle')
st.write(df)

# Chart-Element
st.subheader('Bevölkerungswachstumsdiagramm')
fig, ax = plt.subplots()
ax.plot(df['Jahr'], df['Bevoelkerung'], marker='o')
ax.set_xlabel('Jahr')
ax.set_ylabel('Bevölkerung')
st.pyplot(fig)

# Eingabewidget
st.sidebar.subheader('Wählen Sie den Jahresbereich')
start_jahr = st.sidebar.slider('Startjahr', min_value=2013, max_value=2025 - 1, value=2013)
end_jahr = st.sidebar.slider('Endjahr', min_value=2013, max_value=2024, value=2023)

# Gefilterte Daten
gefilterte_df = df[(df['Jahr'] >= start_jahr) & (df['Jahr'] <= end_jahr)]

# Anzeige der gefilterten Daten
st.sidebar.subheader('Gefilterte Daten')
st.sidebar.write(gefilterte_df)

# Container
st.sidebar.subheader('Zusätzliche Informationen')
with st.sidebar.expander("Bevölkerungswachstumsrate"):
    st.write(f"Die Bevölkerung ist von 2013 bis 2024 um etwa 11% gewachsen.")

# Chat-Element
st.subheader('Chat-Element')
st.text_area('Chatten Sie mit uns...', value='Hier tippen')

# Fußzeile
st.sidebar.markdown("---")
st.sidebar.markdown("Quiz 2 von Shawmiya Ratna")
