import streamlit as st
import pandas as pd
import plotly.express as px


st.title("Mi Aplicación Python")
st.sidebar.title("Parámetros")
st.image("Imagen1.webp", width = 400)
st.sidebar.image("Imagen2.jpg")

modulo = st.sidebar.selectbox("Seleccione un Módulo", ["Módulo 1", "Módulo 2", "Módulo 3"])

if modulo == "Módulo 1":
    st.write("Usted está en el Módulo 1")


    GE = st.number_input("Ingrese la Gravedad Específica", min_value=0.1, max_value=1.0, value=0.87)
    API = (141.5/GE)-131.5
    st.write(API)
elif modulo == "Módulo 2":
    st.write("Usted está en el Módulo 2")
    df=pd.read_excel("Resultados.xlsx")
    st.write(df)
    fig=px.line(df,x="G2", y="API")
    st.write(fig)


else:
    st.write("Usted está en el Módulo 3")
    upload=st.file_uploader("Sube tu archivo .csv o Excel", type=["csv", "xlsx", "xls"])
    if upload is not None:
        st.write("Archivo cargado exitósamente")
        if upload.name.endswith(".csv"):
            df=pd.read_csv(upload)
        elif upload.name.endswith("xlsx"):
            df=pd.read_excel(upload)
        else:
            df=pd.read_excel(upload)
        st.write(df)



    else:
        st.write("Cargue su archivo")