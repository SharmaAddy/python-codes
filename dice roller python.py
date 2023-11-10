#dice roller    
import random
import time
while True:
  print("Devil is rolling the dices......")
  time.sleep(1)
  print("Devil says: ", random.randint(1,6), "and",random.randint(1,12))
  repeat=input("Do you want to roll again? y/n")
  if repeat=="y" or "Y":
    continue
  elif repeat=="n" or "N":
    break
