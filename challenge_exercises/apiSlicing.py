#!/usr/bin/python3
"""tracking the iss using
    api.open-notify.org/astros.json | Alta3 Research"""

import requests

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    print(pokeapi.get('sprites')['front_default'])

    moves = pokeapi.get("moves")
    print(type(moves))
    print(len(moves))

    # printing all moves
    for move in moves:
        print(move['move']['name'])
    
    #  without for loop
    print(f"games in game_indices: {len(pokeapi.get('game_indices'))}")

    #  with for loop

    count = 0
    for game in pokeapi.get('game_indices'):
        count += 1
    print(f"games in game_indices with for loop: {count}")



if __name__ == "__main__":
    main()
