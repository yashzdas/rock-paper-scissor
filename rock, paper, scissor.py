from random import randint

def start_again():
    print('Invalid choice')
    play()

def play_again():
    choose= str(input('Write: y[yes] or n[no]'))
    if choose == 'y':
        play()
    elif choose == 'n':
        print('Thanx for playing. see you..!')
    else:
        print('Wrong keyword..!')
        play_again()

def play():
    values= ['rock', 'paper', 'scissor']
    comp= values[randint(0,2)]
    player= input("Choose:- rock, paper or scissor: ")
    if player not in values:
        start_again()
    '''logics'''    
    print(comp)
    if player == comp:
        print("tied")
    elif player == "rock" and comp == "scissor":
        print("Winner")
    elif player == "scissor" and comp == "paper":
        print("Winner")
    elif player == "paper" and comp == "rock":
        print("Winner")
    elif player == "scissor" and comp == "rock":
        print("Loser")
    elif player == "paper" and comp == "scissor":
        print("Loser")
    elif player == "rock" and comp == "paper":
        print("Loser")
        
    print('Do you want to play again..?')
    play_again()
    
'''calling the function'''
play()
