
print('Welcome to Bear Claw')

def fight(): 
    enemyHp = 100
    playerHp = 100
    playerDmg = 50
    enemyDmg = 25
    turn = 1
    level = 1
    xp = 0
    
    while (enemyHp > 0):
        print(f'turn: {turn}')
        enemyHp -= playerDmg
        print(f'Your opponent has {enemyHp} hp remaining')
        playerHp -= enemyDmg
        print(f'You have {playerHp} hp remaining')
        turn += 1
    else:
        print('You defeated your opponent!')
        xp += 100
    
    if (xp == 100):
        level += 1
        print (f'You are now level: {level}')
        
print('Press any key to attack')
input()
if (input):
    fight()