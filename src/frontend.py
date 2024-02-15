import streamlit as st


class ExcelValidatorUI:

    def __init__(self):
        self.set_page_config()

    @staticmethod
    def set_page_config():
        st.set_page_config(
            page_title="Excel Schema Validator"
        )

    @staticmethod
    def display_header():
        st.title("Insert your spreadsheet for validation")

    @staticmethod
    def upload_file():
        return st.file_uploader("Upload your Excel file here", type=["xlsx"])

    @staticmethod
    def display_results(result, error):
        if error:
            st.error(f"Validation error: {error}")
        else:
            st.success("The Excel file schema is correct!")
