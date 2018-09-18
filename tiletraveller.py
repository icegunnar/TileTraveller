#bý til upphafsstöðu
x_pos = 1
y_pos = 1

while x_pos != 3 and y_pos != 1:
    if(x_pos == 1 and y_pos == 1):
        direction = input('You can travel: (N)orth')
        if direction == 'n':
            x_pos = 1
            y_pos = 2
        else:
            print('invalid input')
    if(x_pos == 1 and y_pos == 2):
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
    if(x_pos == 1 and y_pos == 3):
        direction = input('You can travel: (S)outh or (E)ast')
        if direction == 's':
            x_pos = 1
            y_pos = 2
        elif direction == 'e':
            x_pos = 2
            y_pos = 3
        else:
            print('invalid input')
    if(x_pos == 2 and y_pos == 2):
        direction = input('You can travel: (S)outh or (W)est')
        if direction == 's':
            x_pos = 2
            y_pos = 1
        elif direction == 'w':
            x_pos = 1
            y_pos = 2
        else:
            print('invalid input')
    if(x_pos == 2 and y_pos == 1):
        direction = input('You can travel: (N)orth') 
        if direction == 'n':
            x_pos = 2
            y_pos = 2
        else:
            print('invalid input')
    if(x_pos == 2 and y_pos == 3):
        direction = input('You can travel: (W)est or (E)ast') 
        if direction == 'w':
            x_pos = 3
            y_pos = 3
        elif direction == 'e':
            x_pos = 1
            y_pos = 3
        else:
            print('invalid input')
    if(x_pos == 3 and y_pos == 3):
        direction = input('You can travel: (W)est or (S)outh') 
        if direction == 'w':
            x_pos = 2
            y_pos = 3
        elif direction == 's':
            x_pos = 3
            y_pos = 2
        else:
            print('invalid input')
    if(x_pos == 3 and y_pos == 2):
        direction = input('You can travel: (N)orth or (S)outh') 
        if direction == 'n':
            x_pos = 3
            y_pos = 3
        elif direction == 's':
            x_pos = 3
            y_pos = 1
else:
    print('victory')








        







