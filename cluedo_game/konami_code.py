import streamlit as st

# Définir la séquence du Konami Code
konami_code = ['e', 'z', ' ', 'w', 'i', 'n']
key_sequence = []

def check_konami_code(key_sequence):
    return key_sequence == konami_code

def on_key(key):
    global key_sequence  # Utiliser la variable globale
    key_sequence.append(key)
    if len(key_sequence) > len(konami_code):
        key_sequence.pop(0)  # Supprimer la première touche si la séquence est trop longue
    if check_konami_code(key_sequence):
        st.session_state.konami_activated = True
        st.write("Konami Code activé! Fonctionnalité spéciale débloquée.")
        key_sequence.clear()  # Réinitialiser la séquence après activation
