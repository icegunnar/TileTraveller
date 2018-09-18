#bý til upphafsstöðu
x_pos = 1
y_pos = 1

while pos_x != 3 and pos_y != 1:
    if(pos_x == 1 and pos_y == 1):
        direction = input('You can travel: (N)orth')
        if direction == 'n':
            x_pos = 1
            y_pos = 2
        else:
            print('invalid input')
    if(pos_x == 1 and pos_y == 2):
        direction = input('You can travel: (S)south, (N)orth or (E)ast')
        if direction == 'n':
            x_pos = 1
            y_pos = 3
        elif direction == 's':
            x_pos = 1
            y_pos = 1
        elif direction == 'w':
            x_pos = 2
            y_pos = 2
        else:
            print('invalid input')
    if(pos_x == 1 and pos_y == 3):
        direction = input('You can travel: (S)outh or (E)ast')
        if direction == 's':
            x_pos = 1
            y_pos = 2
        elif direction = 'e':
            x_pos = 2
            y_pos = 3
        else:
            print('invalid input')
    if(pos_x == 2 and pos_y == 2):
        direction = input('You can travel: (S)outh or (W)est')
        if direction == 's':
            x_pos = 2
            y_pos = 1
        elif direction == 'w':
            x_pos = 1
            y_pos = 2
        else:
            print('invalid input')
    if(pos_x == 2 and pos_y == 1):
        direction = input('You can travel: (N)orth') 
        if direction == 'n'
            x_pos = 2
            y_pos = 2
        else:
            print('invalid input')
    if(pos_x == 2 and pos_y == 3):
        direction = input('You can travel: (W)est or (E)ast') 
        if direction == 'w':
            x_pos = 3
            y_pos = 3
        elif direction == 'e':
            x_pos = 1
            y_pos = 3
        else:
            print('invalid input')
    if(pos_x == 3 and pos_y == 3):
        direction = input('You can travel: (W)est or (S)outh') 
        if direction == 'w':
            x_pos = 2
            y_pos = 3
        elif direction == 's':
            x_pos = 3
            y_pos = 2
        else:
            print('invalid input')
    if(pos_x == 3 and pos_y == 2):
        direction = input('You can travel: (N)orth or (S)outh') 
        if direction == 'n'
            x_pos = 3
            y_pos = 3
        elif direction = 's'
            x_pos = 3
            y_pos = 1
else
    print('victory')








        







