# <POKEMON NAME>  | <POKEDEX ID>    | <TYPES>  
# =============== | =============== | ===============
# <IMAGE>         | 'height': 4     | 'speed': 8,
#                 | 'weight': 7     | 'sp. defense': 1
#                 |                 | 'sp. attack': 1
#                 |                 | 'defense': 1
#                 |                 | 'attack': 1
#                 |                 | 'hp': 1
# =============== | =============== | ===============

with open('img2txt-gh-pages/out4.txt', 'r', encoding='utf-16') as f:
    lines = f.readlines()

full = ''.join(lines)
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






# from print_table_lib import print_table

# # header_row = ["This is column number 1", "Column number 2", "col3"]
# # table = [
# #     [3,2, {"whatever":1, "bla":[1,2]}],
# #     [5,"this is a test of wrapping text with the new function",777],
# #     [1,1,1]
# # ]

# # print_table(table, header=header_row,
# #             wrap=False, max_col_width=25, wrap_style='wrap',
# #             row_line=True, fix_col_width=False)

# header_row = ["Bulbasaur", "001", "Poison/Grass"]
# table = [
#     ['\n'.join(draw_lines)],
# ]

# print_table(table,
#             wrap=False, max_col_width=25, wrap_style='wrap',
#             row_line=True, fix_col_width=False)
