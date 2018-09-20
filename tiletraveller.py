#bý til upphafsstöðu
x_pos = 1
y_pos = 1

while True:
    if (x_pos == 1 and y_pos == 1):
        direction1 = input('You can travel: (N)orth.')
        if direction1 == 'n' or direction1 == "N":
            x_pos = 1
            y_pos = 2
        else:
            print('Not a valid direction!')
    if (x_pos == 1 and y_pos == 2):
        direction2 = input('You can travel: (S)south, (N)orth or (E)ast.')
        if direction2 == 'n' or direction2 == 'N':
            x_pos = 1
            y_pos = 3
        elif direction2 == 's' or direction2 == 'S':
            x_pos = 1
            y_pos = 1
        elif direction2 == 'e' or direction2 == 'E':
            x_pos = 2
            y_pos = 2
        else:
            print('Not a valid direction!')
    if (x_pos == 1 and y_pos == 3):
        direction3 = input('You can travel: (S)outh or (E)ast.')
        if direction3 == 's' or direction3 == 'S':
            x_pos = 1
            y_pos = 2
        elif direction3 == 'e'or direction3 == 'E':
            x_pos = 2
            y_pos = 3
        else:
            print('Not a valid direction!')
    if (x_pos == 2 and y_pos == 2):
        direction4 = input('You can travel: (S)outh or (W)est.')
        if direction4 == 's' or direction4 == 'S':
            x_pos = 2
            y_pos = 1
        elif direction4 == 'w'or direction4 == 'W':
            x_pos = 1
            y_pos = 2
        else:
            print('Not a valid direction!')
    if (x_pos == 2 and y_pos == 1):
        direction5 = input('You can travel: (N)orth.') 
        if direction5 == 'n' or direction5 == 'N':
            x_pos = 2
            y_pos = 2
        else:
            print('Not a valid direction!')
    if (x_pos == 2 and y_pos == 3):
        direction6 = input('You can travel: (W)est or (E)ast.') 
        if direction6 == 'e' or direction6 == 'E':
            x_pos = 3
            y_pos = 3
        elif direction6 == 'w'or direction6 == 'W':
            x_pos = 1
            y_pos = 3
        else:
            print('Not a valid direction!')
    if (x_pos == 3 and y_pos == 3):
        direction7 = input('You can travel: (W)est or (S)outh.') 
        if direction7 == 'w' or direction7 == 'W':
            x_pos = 2
            y_pos = 3
        elif direction7 == 's' or direction7 == 'S':
            x_pos = 3
            y_pos = 2
        else:
            print('Not a valid direction!')
    if (x_pos == 3 and y_pos == 2):
        direction8 = input('You can travel: (N)orth or (S)outh.') 
        if direction8 == 'n' or direction8 == 'N':
            x_pos = 3
            y_pos = 3
        elif direction8 == 's' or direction8 == 'S':
            x_pos = 3
            y_pos = 1
            print('Victory!')
            break
        else:
            print("Not a valid direction!")







        







