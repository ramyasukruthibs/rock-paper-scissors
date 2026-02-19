import random

print('========================================')
print('         ROCK PAPER SCISSORS            ')
print('========================================')
while True:
    print('1)✊\n2)✋\n3)✌️\n')
    player=int(input('choose a number:'))

    if player==1:
        print('player chooses ✊')
    elif player==2:
        print('player chooses ✋')
    elif player==3:
        print('player chooses ✌️')
    else:
        print('inavlid')
        continue

    computer=random.randint(1,3)



    if computer==1:
        print('computer chooses ✊')
    elif computer==2:
        print('computer chooses ✋')
    else:
        print('computer chooses✌️')


    if player==computer:
        print('tie\n')
    elif player==1 and computer==2:
        print('hehe you lost~\n')
    elif player==1 and computer==3:
        print('YOU WON!\n')
    elif player==2 and computer==1:
        print('YOU WON!\n')
    elif player==2 and computer==3:
        print('hehe you lost~\n')
    elif player==3 and computer==1:
        print('hehe you lost~\n')
    elif player==3 and computer==2:
        print('YOU WON!\n')
    else:
        print('invalid')