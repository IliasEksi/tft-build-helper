
combinations = [
    {"Bard", "Ezreal", "Galio", "Rumble", "Lillia", "Poppy", "Zoe"},
    {"Bard", "Hwei", "Rumble", "Zilean", "Jax", "Warwick", "Zoe"},
    {"Bard", "Hwei", "Rumble", "Zilean", "Poppy", "Warwick", "Zoe"},
    {"Bard", "Ezreal", "Neeko", "Rumble", "Blitzcrank", "Jayce", "Zoe"},
    {"Bard", "Ezreal", "Neeko", "Rumble", "Jayce", "Warwick", "Zoe"},
    {"Bard", "Ezreal", "Cassiopeia", "Galio", "Rumble", "Ziggs", "Zoe"},
    {"Bard", "Ezreal", "Galio", "Nunu", "Rumble", "Poppy", "Zoe"},
    {"Bard", "Ezreal", "Galio", "Rumble", "Zilean", "Jax", "Zoe"},
    {"Bard", "Ezreal", "Galio", "Rumble", "Zilean", "Poppy", "Zoe"},
    {"Bard", "Hwei", "Ahri", "Rumble", "Zilean", "Jax", "Warwick"},
    {"Bard", "Hwei", "Cassiopeia", "Rumble", "Zilean", "Warwick", "Zoe"},
    {"Bard", "Neeko", "Galio", "Rumble", "Tristana", "Jayce", "Zoe"},
    {"Bard", "Neeko", "Galio", "Rumble", "Zilean", "Jayce", "Zoe"},
    {"Ezreal", "Hecarim", "Ahri", "Galio", "Rumble", "Poppy", "Zoe"},
    {"Ezreal", "Jinx", "Galio", "Rumble", "Shyvana", "Jayce", "Nomsy"},
    {"Bard", "Ezreal", "Hecarim", "Galio", "Rumble", "Poppy", "Zoe"},
    {"Bard", "Ezreal", "Neeko", "Galio", "Rumble", "Elise", "Zoe"},
    {"Bard", "Ezreal", "Neeko", "Galio", "Rumble", "Jayce", "Zoe"},
    {"Bard", "Ezreal", "Neeko", "Rumble", "Zilean", "Jayce", "Zoe"},
    {"Bard", "Ezreal", "Shen", "Galio", "Rumble", "Poppy", "Zoe"},
    {"Bard", "Ezreal", "Cassiopeia", "Galio", "Rumble", "Syndra", "Zoe"},
    {"Bard", "Ezreal", "Cassiopeia", "Galio", "Rumble", "Zilean", "Zoe"},
    {"Bard", "Hwei", "Neeko", "Galio", "Rumble", "Jayce", "Zoe"},
    {"Bard", "Hwei", "Neeko", "Rumble", "Zilean", "Warwick", "Zoe"},
    {"Bard", "Hwei", "Vex", "Rumble", "Zilean", "Warwick", "Zoe"},
    {"Bard", "Jinx", "Neeko", "Shyvana", "Zilean", "Nomsy", "Zoe"},
    {"Bard", "Neeko", "Swain", "Rumble", "Zilean", "Warwick", "Zoe"},
    {"Hwei", "Jinx", "Swain", "Rumble", "Shyvana", "Nomsy", "Warwick"},
    {"Bard", "Ezreal", "Mordekaiser", "Neeko", "Rumble", "Jayce", "Zoe"},
    {"Bard", "Ezreal", "Neeko", "Galio", "Rumble", "Shyvana", "Zoe"},
    {"Bard", "Ezreal", "Neeko", "Galio", "Rumble", "Zilean", "Zoe"},
    {"Bard", "Ezreal", "Vex", "Galio", "Rumble", "Zilean", "Zoe"},
    {"Bard", "Hecarim", "Hwei", "Ahri", "Rumble", "Zilean", "Warwick"},
    {"Bard", "Hecarim", "Shen", "Ahri", "Akali", "Zilean", "Jax"},
    {"Bard", "Hwei", "Neeko", "Swain", "Rumble", "Warwick", "Zoe"},
    {"Bard", "Hwei", "Vex", "Ahri", "Rumble", "Zilean", "Warwick"},
    {"Bard", "Jinx", "Neeko", "Swain", "Zilean", "Twitch", "Zoe"},
    {"Bard", "Ezreal", "Neeko", "Swain", "Galio", "Rumble", "Zoe"},
    {"Bard", "Hwei", "Neeko", "Swain", "Rumble", "Zilean", "Zoe"} 
]

validchampions = {"Bard", "Ezreal", "Hwei", "Neeko", "Jinx", "Swain",
                   "Mordekaiser", "Vex", "Hecarim", "Galio", "Rumble", "Cassiopeia",
                   "Zilean", "Ahri", "Akali", "Tristana", "Shyvana", "Lillia", "Poppy", "Zoe", "Jax", "Warwick",
                   "Blitzcrank", "Jayce", "Ziggs", "Elise", "Nomsy"}

def findComps():
    ownedchamps = set()  
    while True:
        x = input("What Champions do you have? (Type 'done' to finish): ").capitalize()
        if x.lower() == 'done': 
            break
        elif x in validchampions:
            ownedchamps.add(x) 
        else:
            print(f"{x} is not a valid champion or not part of the combinations.")
    
    return ownedchamps

def combwithbiggestoverlap(ownedchamps):
    overlap_list = []

    
    for comb in combinations:
        overlap = len(ownedchamps & comb)  
        overlap_list.append((comb, overlap)) 

    
    overlap_list.sort(key=lambda x: x[1], reverse=True)

    return overlap_list


print("This only shows comps that use up to 3 cost champs and are at lvl 7, enter all your champs one by one or only a couple  important ones like bard, to be more flexible")
ownedchamps = findComps()
overlap_list = combwithbiggestoverlap(ownedchamps)


if overlap_list:
    print("Combinations ranked by overlap:\n")
    counter = 0
    for comb, overlap in overlap_list:
        print(f"Combination: {comb}, Overlap: {overlap}\n")
        counter = counter +1 
        if counter > 9:
            break
else:
    print("No combination has any overlap with your owned champions.")


def mainfun():
    x = input("Start again? (y/n):   ")
    if x == "y":
        ownedchamps = findComps()
        overlap_list = combwithbiggestoverlap(ownedchamps)

        if overlap_list:
              print("Combinations ranked by overlap:\n")
              counter = 0
              for comb, overlap in overlap_list:
                   print(f"Combination: {comb}, Overlap: {overlap}\n")
                   counter = counter +1 
                   if counter > 9:
                     break
        else:
                print("No combination has any overlap with your owned champions.")
        mainfun()


mainfun()

input("Press Enter to exit...")

