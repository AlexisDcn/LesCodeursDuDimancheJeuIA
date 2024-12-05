import streamlit as st

def check_konami_code(key_sequence):
    konami_code = ['e', 'z', ' ', 'w', 'i', 'n']
    return key_sequence == konami_code

key_sequence = []

def on_key(key):
    key_sequence.append(key)
    if len(key_sequence) > len(konami_code):
        key_sequence.pop(0)  # Supprimer la première touche si la séquence est trop longue
    if check_konami_code(key_sequence):
        st.session_state.konami_activated = True
        st.write("Konami Code activé! Fonctionnalité spéciale débloquée.")
        key_sequence.clear()  # Réinitialiser la séquence après activation
