import random

adjectives = [
    'Silent',
    'Shadow',
    'Iron',
    'Crimson',
    'Ghost',
    'Frozen',
    'Steel',
    'Black'
]

nouns = [
    'Fox',
    'Wolf',
    'Raven',
    'Falcon',
    'Viper',
    'Tiger',
    'Phantom',
    'Panther'
]

def generate_nickname():
    random_name = random.choice(adjectives) + random.choice(nouns)
    return random_name