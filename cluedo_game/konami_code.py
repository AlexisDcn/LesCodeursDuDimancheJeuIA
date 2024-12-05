import streamlit as st

def check_konami_code(key_sequence):
    konami_code = ['up', 'up', 'down', 'down', 'left', 'right', 'left', 'right', 'b', 'a']
    return key_sequence == konami_code

key_sequence = []

def on_key(key):
    key_sequence.append(key)
    if check_konami_code(key_sequence):
        st.write("Konami Code activé! Fonctionnalité spéciale débloquée.")
