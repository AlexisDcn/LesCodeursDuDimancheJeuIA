import streamlit as st
from cluedo_agent import CluedoAgent
from game_logic import initialize_game
from konami_code import check_konami_code, on_key

st.title("Cluedo: Mystère des Océans")

agent = CluedoAgent()

st.sidebar.title("Menu")
st.sidebar.write("Utilisez ce menu pour naviguer dans le jeu.")

if 'game_state' not in st.session_state:
    st.session_state.game_state = initialize_game()

st.write("Bienvenue dans le jeu Cluedo: Mystère des Océans!")

player_question = st.text_input("Posez une question à l'agent IA:")
if st.button("Obtenir un indice"):
    hint = agent.give_hint(player_question)
    st.write(hint)

if st.button("Faire un mouvement"):
    move = agent.make_move(st.session_state.game_state)
    st.write(move)

st.write("Appuyez sur les touches pour activer le Konami Code.")
st.text_input("", key="key_input", on_change=on_key)
