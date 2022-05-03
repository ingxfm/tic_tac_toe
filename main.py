controls = {
    '1st_line': [1, 2, 3],
    '2nd_line': [4, 5, 6],
    '3rd_line': [7, 8, 9],
}


print('To play TTT (tic-tac-toe), press a number from 1 to 9.\n'
      'From 1 to 3, for the first line, from left to right.\n'
      'From 4 to 6, for the second line, from left to right.\n'
      'From 7 to 9, for the third line, from left to right.\n')

for key in controls:
    print(f'{controls[key]}')

print('\n')

play = input('Press a number key from 1 to 9 to select a position: ')

value = 0
for key in controls:
    if int(play) in controls[key]:
        controls[key][controls[key].index(int(play))] = 'x'
        for key in controls:
            print(f'{controls[key]}')
        print('yeah')
