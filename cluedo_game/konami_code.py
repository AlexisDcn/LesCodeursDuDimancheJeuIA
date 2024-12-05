import streamlit as st

def check_konami_code(key_sequence):
    konami_code = ['e', 'z', ' ', 'w', 'i', 'n']
    return key_sequence == konami_code

key_sequence = []

def on_key(key):
    key_sequence.append(key)
    if check_konami_code(key_sequence):
        st.write("Konami Code activé! Fonctionnalité spéciale débloquée.")
        # Réinitialiser la séquence après activation
        key_sequence.clear()
