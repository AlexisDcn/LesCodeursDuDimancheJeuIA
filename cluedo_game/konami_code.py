def check_konami_code(key_sequence):
    konami_code = ['e', 'z', ' ', 'w', 'i', 'n']
    return key_sequence == konami_code

def on_key(key_sequence):
    if check_konami_code(key_sequence):
        return True
    return False

def reveal_culprit(game_state):
    return f"Le coupable est {game_state['solution']['suspect']} avec {game_state['solution']['weapon']} à {game_state['solution']['location']}."
