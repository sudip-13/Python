import random
ls=["snake","water","gun"]
s=random.randint(0,2)
pla=int(input("Enter : \n0: for snake\n1:for water\n2:for gun\n"))
win=[["Drawn","Won","lost"],["lost","Drawn","Won"],["Won","lost","Drawn"]]
print(f"the match has {win[pla][s]} by player \nbecause System choose {ls[s]} and player choose {ls[pla]}")