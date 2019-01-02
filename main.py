import os
from prompt_toolkit import prompt

logo_sprite = 'sprites/logo/ansilogo.txt'

def clear_screen():
    os.system('cls')

def draw_logo():
    with open(logo_sprite, 'r') as f:
        full = ''.join(f.readlines())
    draw_lines = full.split('\n')
    print(full)
    print()

def main_screen():
    draw_logo()
    print('Main Screen')

def help_screen():
    draw_logo()
    print('Help')

def pokemon_screen(pokemon_name):
    with open('img2txt-gh-pages/out4.txt', 'r', encoding='utf-16') as f:
        full = ''.join(f.readlines())
    draw_lines = full.split('\n')

    col1 = ['Bulbasaur', *draw_lines]
    col2 = ['001', 'Height: 4', 'Weight: 7']
    col3 = ['Poison/Grass', 'speed: 8', 'sp. defense: 1', 'sp. attack: 1', 'defense: 1', 'attack: 1', 'hp: 1']
    table = [col1, col2, col3]

    max_rows = max([len(col) for col in table])
    table = [ col+['']*(max_rows-len(col)) for col in table ]

    for i, row in enumerate(zip(*table)):
        for cell in row:
            print(cell.ljust(25), '|',len(row[0]), end='')
        print()
        if i==0:
            print('-'*80)
    print()

def type_screen(type_name):
    print('Type screen', type_name)

def ability_screen(ability_name):
    print('Ability screen', ability_name)

user_input = 'main'
screen, arg = '', ''
while True:
    clear_screen()

    if user_input == 'main':
        main_screen()
    elif user_input == 'help':
        help_screen()
    elif user_input == 'exit':
        exit(0)
    elif ':' in user_input:
        try:
            screen, arg = user_input.split(':')
        except ValueError:
            print('Incorrect command')

        if screen =='pokemon':
            pokemon_screen(arg)
        elif screen == 'type':
            type_screen(arg)
        elif screen == 'ability':
            ability_screen(arg)
        else:
            print('Incorrect command')
    else:
        print('Incorrect command')

    # print(user_input)
    user_input = prompt('Pokedex> ')
