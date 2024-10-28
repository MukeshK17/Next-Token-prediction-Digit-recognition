# import streamlit as st
# # from model import *
# def calc():
#     oper = input()
#     ans = oper[0]+oper[-1]
#     return ans

import streamlit as st

if 'sum' not in st.session_state:
    st.session_state.sum = ''

def sum():
    result = st.session_state.a + st.session_state.b
    st.session_state.sum = result

col1, col2 = st.columns(2)
col1.title('Sum:')
if isinstance(st.session_state.sum, float):
    col2.title(f'{st.session_state.sum:.2f}')

with st.form('addition'):
    st.number_input('a', key='a', min_value=0, max_value=9, step=1)
    st.number_input('b', key='b', min_value=0, max_value=9, step=1)
    st.form_submit_button('Add', on_click=sum)
