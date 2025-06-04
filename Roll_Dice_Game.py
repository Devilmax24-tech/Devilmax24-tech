
import random

while True:
  print('\t\t\t\t\t\t"Welcome to Roll Dice Game🎲🎲"')
  select_user = input('If You want to play the Game!(y/n): ').lower()
  if select_user =='y':
    select_multiple_user = input('Do you want to play with patner(y/n): ').lower()
    print("\t\t\t\t\t\t\t\tLet's play!")

    if select_multiple_user == 'y':

      dice1 = random.randint(1,6)
      dice2 = random.randint(1,6)
      print(f'player_1: {dice1}')
      print(f'Player_2: {dice2}')
    elif select_multiple_user == 'n':
      print("Single player Game🎲")
      dice0 = random.randint(1,6)
      print(f'Dice_Turn: {dice0}')
      if dice1>dice2:
        result = (f'Player_1 win Game by: {dice1-dice2}')
      elif dice1<dice2:
        result = (f'Player_2 win Game by: {dice2-dice1}')
      else:
        result = 'Game Tie🎲'
      print('Thanks for playing😁')
    else:
      print('Invalid Choice!')
      break
  elif select_user =='n':
    print('Thanks for playing😁')
    if dice1>dice2:
        result = (f'Player_1 win Game by: {dice1-dice2}')
    elif dice1<dice2:
        result = (f'Player_2 win Game by: {dice2-dice1}')
    else:
        result = 'Game Tie🎲'
    break
  else:
        print('Invalid Choice!')
      
