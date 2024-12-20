import os
import requests
import random

class CluedoAgent:
    def __init__(self):
        self.knowledge = {
            'suspects': ['Dr. Plankton', 'Captain Nemo', 'Prof. Oceanus'],
            'weapons': ['Filet de pêche', 'Harpon', 'Bouteille de plastique'],
            'locations': ['Récif de corail', 'Épave de navire', 'Plage polluée']
        }
        self.api_url = "http://127.0.0.1:11435/api/generate"  # Remplacez par l'URL de votre API Ollama
        self.api_key = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBhFGJ1X36XUGvFhWiuBmOej9cxAt1p+fooqXJ+9rjWs"  # Remplacez par votre clé API

    def give_hint(self, game_state):
        hints = [
            f"Le suspect pourrait être {game_state['solution']['suspect']}.",
            f"L'arme pourrait être {game_state['solution']['weapon']}.",
            f"Le lieu pourrait être {game_state['solution']['location']}."
        ]
        return random.choice(hints)

    def make_move(self, game_state):
        move_type = random.choice(['move', 'accusation'])
        if move_type == 'move':
            location = random.choice(game_state['locations'])
            return {'type': 'move', 'location': location}
        else:
            suspect = random.choice(game_state['suspects'])
            weapon = random.choice(game_state['weapons'])
            location = random.choice(game_state['locations'])
            return {
                'type': 'accusation',
                'accusation': {
                    'suspect': suspect,
                    'weapon': weapon,
                    'location': location
                }
            }

    def ask_question(self, question):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        data = {
            "model": "phi-3",
            "prompt": question
        }
        response = requests.post(self.api_url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json().get('response', "Désolé, je n'ai pas pu comprendre votre question.")
        else:
            return "Désolé, je n'ai pas pu comprendre votre question."
