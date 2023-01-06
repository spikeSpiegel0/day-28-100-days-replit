import random, os, time

def rollDice(side):
  result = random.randint(1,side)
  return result
  
def healthStats():
  six_sided_roll = random.randint(1,6)
  twelve_sided_roll = random.randint(1,12)
  healthStat = int(round((six_sided_roll*twelve_sided_roll)/2+10,0))
  return healthStat

def strenghtStats():
  six_sided_roll = random.randint(1,6)
  eight_sided_roll = random.randint(1,8)
  strenghtStat = int(round((six_sided_roll*eight_sided_roll)/2+12,0))
  return strenghtStat

print("⚔️ BATTLE TIME ⚔️")
print()

player_1 = input("Name your Legend: \n")
player_1type = input("Character Type (Human, Elf, Wizard, Orc):\n")
print()
print(player_1)
player_1health = healthStats()
print("HEALTH: ", player_1health)
player_1strength = strenghtStats()
print("STRENGTH: ", player_1strength)
print()
print("Who are they battling?")
print()
player_2 = input("Name your Legend: \n")
player_2type = input("Character Type (Human, Elf, Wizard, Orc):\n")
print()
print(player_2)
player_2health = healthStats()
print("HEALTH: ", player_2health)
player_2strength = strenghtStats()
print("STRENGTH: ", player_2strength)
print()
   
time.sleep(3)
os.system("clear")
 
print("The battle begins!")
print()
round = 1

while True:
  player1dice = rollDice(6)
  player2dice = rollDice(6)
  
  difference = abs(player_1strength - player_2strength) + 1

  if player1dice > player2dice:
    player_1strength +=1
    player_2health -= difference
    print(player_1, "wins the first blow")
    print(player_2, "takes a hit, with", difference, "damage")
    print()
  elif player2dice > player1dice:
    player_2strength +=1
    player_1health -= difference
    print(player_2, "wins the first blow")
    print(player_1, "takes a hit, with", difference, "damage")
    print()
  else:
    print("It's a tie")
    print()

  
  round +=1
  time.sleep(3)
  os.system("clear") 

  print(player_1)
  print("HEALTH: ", player_1health)
  print()
  print(player_2)
  print("HEALTH: ", player_2health)
  print()
  
  
  if player_1health <= 0:
    print("Game over", player_2,"won!")
    break
  elif player_2health <= 0:
    print("Game over", player_1,"won")
    break
  else:
    print("And they are both standing for the nex round!")