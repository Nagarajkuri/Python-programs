import random
while True:
    choices=('r','p','s')
    computer=random.choice(choices)
    player=None

    while player not in choices:
        player=input('r,p,s?: ').lower()
    if player==computer:

        print("computer: ",computer)
        print('player: ',player)
        print('tie')
    elif player=='r':
        if computer=='p':
            print("computer: ",computer)
            print('player: ',player)
            print('you lose!')
        if computer=='s':
            print("computer: ",computer)
            print('player: ',player)
            print('you win!')

    elif player=='s':
        if computer=='r':
            print("computer: ",computer)
            print('player: ',player)
            print('you lose!')
        if computer=='p':
            print("computer: ",computer)
            print('player: ',player)
            print('you win!')
    elif player=='p':
        if computer=='s':
            print("computer: ",computer)
            print('player: ',player)
            print('you lose!')
        if computer=='r':
            print("computer: ",computer)
            print('player: ',player)
            print('you win!')
    play_again=input("play again? (yes/no): ").lower()
    if play_again !='yes':
        break
print("BYE")