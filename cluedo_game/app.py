import streamlit as st
from cluedo_agent import CluedoAgent
from game_logic import initialize_game, update_game_state, make_move, give_hint
from konami_code import reveal_culprit

# Initialisation de l'agent IA
agent = CluedoAgent()

# Initialisation de l'état du jeu
if 'game_state' not in st.session_state:
    st.session_state.game_state = initialize_game()

# Initialisation de l'état pour le Konami Code
if 'menu_clicks' not in st.session_state:
    st.session_state.menu_clicks = 0
if 'konami_activated' not in st.session_state:
    st.session_state.konami_activated = False
if 'last_click_time' not in st.session_state:
    st.session_state.last_click_time = 0

# Menu de navigation dans la barre latérale
st.sidebar.title("Menu")
if st.sidebar.button("MENU", key="menu_button"):
    import time
    current_time = time.time()
    time_since_last_click = current_time - st.session_state.last_click_time
    st.session_state.last_click_time = current_time

    if time_since_last_click <= 2:  # Si les clics sont espacés de moins de 2 secondes
        st.session_state.menu_clicks += 1
    else:  # Réinitialiser si le délai est trop long
        st.session_state.menu_clicks = 1

    # Vérifier si le Konami Code est activé
    if st.session_state.menu_clicks >= 5:  # 5 clics rapides
        st.session_state.konami_activated = True
        st.sidebar.write("Konami Code activé! Fonctionnalité spéciale débloquée.")
        st.sidebar.write(reveal_culprit(st.session_state.game_state))
        st.session_state.menu_clicks = 0  # Réinitialiser après activation

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

# Page d'aide
elif selected_menu == "Aide":
    st.title("Cluedo: Mystère des Océans - Aide")
    st.write("## Comment jouer")
    st.write("- Posez des questions à l'agent IA pour obtenir des indices.")
    st.write("- Faites des mouvements pour résoudre le mystère.")
    st.write("## Konami Code")
    st.write("- Cliquez cinq fois rapidement sur le bouton 'MENU' dans la barre latérale pour activer le Konami Code.")
