import streamlit as st
from cluedo_agent import CluedoAgent
from game_logic import initialize_game, update_game_state, make_move, give_hint
from konami_code import check_konami_code, on_key

# Initialisation de l'agent IA
agent = CluedoAgent()

# Initialisation de l'état du jeu
if 'game_state' not in st.session_state:
    st.session_state.game_state = initialize_game()

# Initialisation de l'état du Konami Code
if 'konami_activated' not in st.session_state:
    st.session_state.konami_activated = False
if 'key_sequence' not in st.session_state:
    st.session_state.key_sequence = []

# Menu de navigation dans la barre latérale
st.sidebar.title("Menu")
st.sidebar.write("Utilisez ce menu pour naviguer dans le jeu.")

menu_options = ["Accueil", "Jouer", "Aide"]
selected_menu = st.sidebar.selectbox("Aller à", menu_options)

# Page d'accueil
if selected_menu == "Accueil":
    st.title("Cluedo: Mystère des Océans")
    st.write("Bienvenue dans le jeu Cluedo: Mystère des Océans!")
    st.write("Utilisez le menu pour naviguer et commencer à jouer.")

# Page de jeu
elif selected_menu == "Jouer":
    st.title("Cluedo: Mystère des Océans - Jouer")

    st.write("Bienvenue dans le jeu Cluedo: Mystère des Océans!")

    player_question = st.text_input("Posez une question à l'agent IA:")
    if st.button("Obtenir une réponse"):
        response = agent.ask_question(player_question)
        st.write(response)

    location = st.selectbox("Choisissez un lieu pour vous déplacer:", st.session_state.game_state['locations'])
    if st.button("Déplacer"):
        move = make_move(st.session_state.game_state, 'move', location=location)
        st.session_state.game_state = update_game_state(st.session_state.game_state, move)
        st.write(f"Vous vous êtes déplacé vers {location}.")

    suspect = st.selectbox("Choisissez un suspect:", st.session_state.game_state['suspects'])
    weapon = st.selectbox("Choisissez une arme:", st.session_state.game_state['weapons'])
    location = st.selectbox("Choisissez un lieu:", st.session_state.game_state['locations'])
    if st.button("Faire une accusation"):
        move = make_move(st.session_state.game_state, 'accusation', suspect=suspect, weapon=weapon, location=location)
        st.session_state.game_state = update_game_state(st.session_state.game_state, move)
        if 'winner' in st.session_state.game_state:
            st.write(f"Félicitations, {st.session_state.game_state['winner']}! Vous avez résolu le mystère!")
        else:
            st.write("Votre accusation est incorrecte. Essayez encore.")

    # Capturer les entrées de l'utilisateur pour le Konami Code
    key_input = st.text_input("Appuyez sur les touches pour activer le Konami Code:", key="key_input")
    if key_input:
        st.session_state.key_sequence.append(key_input[-1])  # Ajouter la dernière touche entrée
        if len(st.session_state.key_sequence) > 6:  # La séquence du Konami Code a 6 touches
            st.session_state.key_sequence.pop(0)  # Supprimer la première touche si la séquence est trop longue
        if on_key(st.session_state.key_sequence):
            st.write("Konami Code activé! Fonctionnalité spéciale débloquée.")
            st.session_state.key_sequence = []  # Réinitialiser la séquence après activation

# Page d'aide
elif selected_menu == "Aide":
    st.title("Cluedo: Mystère des Océans - Aide")
    st.write("## Comment jouer")
    st.write("- Posez des questions à l'agent IA pour obtenir des indices.")
    st.write("- Faites des mouvements pour résoudre le mystère.")
    st.write("## Konami Code")
    st.write("- Pour activer le Konami Code, appuyez sur les touches suivantes dans cet ordre: e, z, espace, w, i, n.")
