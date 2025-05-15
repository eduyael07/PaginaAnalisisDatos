import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



data = pd.read_csv("Computos2006-Presidente.txt", sep="|") #Cargo la base da datos
print("Numero de entradas: ", data.shape)

st.markdown("# Analisis de datos para las votaciones del 2006")
st.markdown("Primeor cargamos los datos")
st.markdown(f"Numero de entradas{data.shape}")

id2state = {1: 'Aguascalientes', 2:'Baja California', 3: 'Baja California Sur', 4: 'Campeche',
           5: 'Coahuila', 6: 'Colima', 7: 'Chiapas', 8: 'Chihuahua', 9:'CDMX', 10: 'Durango',
           11: 'Guanajuato', 12: 'Guerrero', 13: 'Hidalgo', 14: 'Jalisco', 15: 'México',
           16: 'Michoacán', 17: 'Morelos', 18: 'Nayarit', 19: 'Nuevo León', 20: 'Oaxaca',
           21: 'Puebla', 22: 'Querétaro', 23: 'Quintana Roo', 24: 'San Luis Potosí',
           25: 'Sinaloa', 26: 'Sonora', 27: 'Tabasco', 28: 'Tamaulipas', 29: 'Tlaxcala',
           30: 'Veracruz', 31: 'Yucatán', 32: 'Zacatecas'} 

data["ID_ESTADO"] = data["ID_ESTADO"].apply(lambda x: id2state[x])
datos10 = data.head(10)
print(datos10['ID_ESTADO'])
st.table(datos10['ID_ESTADO'])
data.rename(columns={'ID_ESTADO':'ESTADO'}, inplace=True)
len(data.ESTADO.unique())
st.markdown(f"Los estados que votaron son: {len(data.ESTADO.unique())}")

votoExtranjero=data[data["TIPO_CANDIDATURA"]==6]
votoLocal=data[data["TIPO_CANDIDATURA"]==1]

