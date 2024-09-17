
import random as rd

a1 = ""
a2 = ""
a3 = ""
b1 = ""
b2 = ""
b3 = ""
c1 = ""
c2 = ""
c3 = ""

def tictactoe():
    print(f'\n {a1}     |       {a2}        |{a3}  ')
    print("_   _   _   _   _   _   _   _    ")
    print(f'\n {b1}     |       {b2}        |{b3}  ')
    print("_   _   _   _   _   _   _   _    ")
    print(f'\n {c1}     |       {c2}        |{c3}  ')

user_input = []
winner1 = [[1,2,3],[1,4,7],[1,5,9],[7,8,9],[7,5,3],[3,6,9],[2,5,8],[4,5,6]]
user_input1 = []


def winner(user_input):
    for n in range(len(winner1)):
        count = 0
        for i in winner1[n]:
            if len(user_input) >= 3:
                k = -1
                for j in range(len(user_input)):
                    k = k+1
                    if i == user_input[k]:
                        count = count + 1
                        if count == 3:
                            return "win"
                        break
                    

for i in range(9):
        
        user = int(input("Enter The Number(player 1)X:"))

        if user == 1:
            a1 = 'X'
            user_input.append(user) 
        elif user == 2:
            a2 = 'X'
            user_input.append(user) 

        elif user == 3:
            a3 = 'X'
            user_input.append(user) 

        elif user == 4:
            b1 = 'X'
            user_input.append(user) 

        elif user == 5:
            b2 = 'X'
            user_input.append(user) 

        elif user == 6:
            b3 = 'X'
            user_input.append(user) 

        elif user == 7:
            c1 =  'X'
            user_input.append(user) 

        elif user == 8:
            c2 = 'X'
            user_input.append(user) 

        elif user == 9:
            c3 = 'X'
            user_input.append(user) 

        tictactoe()

        if winner(user_input) == 'win':
            print("Player 1 win")
            break
    
        user = int(input("Enter The Number(player 2)O:"))

        if user == 1:
            a1 = 'O'
            user_input1.append(user) 
        elif user == 2:
            a2 = 'O'
            user_input1.append(user) 

        elif user == 3:
            a3 = 'O'
            user_input1.append(user) 

        elif user == 4:
            b1 = 'O'
            user_input1.append(user) 

        elif user == 5:
            b2 = 'O'
            user_input1.append(user) 

        elif user == 6:
            b3 = 'O'
            user_input1.append(user) 

        elif user == 7:
            c1 =  'O'
            user_input1.append(user) 

        elif user == 8:
            c2 = 'O'
            user_input1.append(user) 

        elif user == 9:
            c3 = 'O'
            user_input1.append(user) 

        tictactoe()
        
        if winner(user_input1) == 'win':
            print("Player 2 win")
            break

        if len(user_input) + len(user_input1) == 9:
            print('DRAW')
            break

