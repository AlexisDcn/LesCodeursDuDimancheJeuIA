import random

suspects = ['Dr. Plankton', 'Captain Nemo', 'Prof. Oceanus']
weapons = ['Filet de pêche', 'Harpon', 'Bouteille de plastique']
locations = ['Récif de corail', 'Épave de navire', 'Plage polluée']

def initialize_game():
    solution = {
        'suspect': random.choice(suspects),
        'weapon': random.choice(weapons),
        'location': random.choice(locations)
    }

    game_state = {
        'players': ['Joueur 1', 'Joueur 2'],
        'suspects': suspects,
        'weapons': weapons,
        'locations': locations,
        'solution': solution,
        'current_player': 'Joueur 1',
        'current_location': random.choice(locations),
        'accusations': []
    }

    return game_state

def update_game_state(game_state, move):
    if move['type'] == 'move':
        game_state['current_location'] = move['location']
    elif move['type'] == 'accusation':
        game_state['accusations'].append(move['accusation'])
        if move['accusation'] == game_state['solution']:
            game_state['winner'] = game_state['current_player']

    game_state['current_player'] = 'Joueur 2' if game_state['current_player'] == 'Joueur 1' else 'Joueur 1'

    return game_state

def make_move(game_state, move_type, **kwargs):
    move = {'type': move_type}
    if move_type == 'move':
        move['location'] = kwargs.get('location')
    elif move_type == 'accusation':
        move['accusation'] = {
            'suspect': kwargs.get('suspect'),
            'weapon': kwargs.get('weapon'),
            'location': kwargs.get('location')
        }
    return move

def give_hint(game_state):
    hints = [
        f"Le suspect pourrait être {game_state['solution']['suspect']}.",
        f"L'arme pourrait être {game_state['solution']['weapon']}.",
        f"Le lieu pourrait être {game_state['solution']['location']}."
    ]
    return random.choice(hints)
