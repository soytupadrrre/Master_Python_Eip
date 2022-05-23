import streamlit as st
from rest_iris import RestIris

def view(iris: RestIris):
    st.header("Dashboard de Eliminar Datos")
    st.subheader("Eliminar datos de la base de datos")
    # Get data from user
    id = st.number_input("ID", min_value=1)
    # Delete data
    if st.button("Eliminar datos"):
        iris.delete_by_id({'id': id})
        st.success("Datos eliminados correctamente del registro: {}".format(id))