import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Colectivo 221",
    page_icon="🚌",
    layout="centered"
)

st.title("🚌 Colectivo 221")
st.caption("Mar del Plata ↔ Santa Clara")

st.markdown("### 📍 Reporte ciudadano")

parada = st.text_input("Parada donde estás")
sentido = st.selectbox("Sentido del colectivo", ["Mar del Plata → Santa Clara", "Santa Clara → Mar del Plata"])
estado = st.selectbox("Estado", ["Recién pasó", "Está llegando", "Estoy arriba"])

if st.button("Enviar reporte"):
    if parada:
        st.success("✅ Reporte enviado")
        st.write({
            "parada": parada,
            "sentido": sentido,
            "estado": estado,
            "hora": datetime.now().strftime("%H:%M")
        })
    else:
        st.warning("⚠️ Completá la parada")
