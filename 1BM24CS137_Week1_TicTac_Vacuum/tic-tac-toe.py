def check(B):
    if B[0][0]==B[0][1] and B[0][0]==B[0][2]:
        return B[0][0]
    elif B[1][0]==B[1][1] and B[1][0]==B[1][2]:
        return B[1][0]
    elif B[2][0]==B[2][1] and B[2][0]==B[2][2]:
        return B[2][0]
    elif B[0][0]==B[1][0] and B[1][0]==B[2][0]:
        return B[0][0]
    elif B[0][1]==B[1][1] and B[1][1]==B[2][1]:
        return B[0][1]
    elif B[0][2]==B[1][2] and B[1][2]==B[2][2]:
        return B[0][2]
    elif B[0][0]==B[1][1] and B[1][1]==B[2][2]:
        return B[0][0]
    elif B[0][2]==B[1][1] and B[1][1]==B[2][0]:
        return B[0][2]
    else:
        return 'N'

def play(player,B):
    x = int(input("Enter x position : "))
    y = int(input("Enter y position : "))
    if B[x-1][y-1] == 'E':
        B[x-1][y-1] = player
    else:
        print("Position occupied! Enter position again")
        play(player,B)

def display(B):
    print(f" {B[0][0]} | {B[0][1]} | {B[0][2]}")
    print(" ---------")
    print(f" {B[1][0]} | {B[1][1]} | {B[1][2]}")
    print(" ---------")
    print(f" {B[2][0]} | {B[2][1]} | {B[2][2]}")

B = [['E','E','E'],['E','E','E'],['E','E','E']]

current = input("1st player (X or O) : ")

for i in range(9):
    display(B)
    print(f"\nPlayer {current}'s Turn")
    play(current,B)
    check_output = check(B)
    if check_output == 'X' or check_output == 'O':
        display(B)
        print(f"Player {current} wins!")
        break
    if current == 'X':
        current = 'O'
    elif current == 'O':
        current = 'X'

if check(B) == 'N':
    display(B)
    print("Game is a draw!")
