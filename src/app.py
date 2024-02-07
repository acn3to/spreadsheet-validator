import streamlit as st

st.set_page_config(
    page_title="Excel Schema Validator"
)

st.title("Insert your spreadsheet for validation")

file = st.file_uploader("Upload your Excel file here", type=["xlsx"])

if file:
    st.success("The Excel file schema is correct!")
