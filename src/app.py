import streamlit as st
import pandas as pd
import numpy as np

st.title('Our First App with Streamlit')

st.markdown('**Hello world!** 🌍')

st.write('This is a demonstration of some Streamlit functionalities.')

input_text = st.text_input('Type something here:')

st.write(f'You typed: {input_text}')

selected_number = st.slider('Choose a number', 0, 100, 50)

st.write(f'You chose the number: {selected_number}')

data = pd.DataFrame({
    'columns': ['A', 'B', 'C', 'D', 'E'],
    'values': np.random.randn(5)
})

st.line_chart(data.set_index('columns'))
