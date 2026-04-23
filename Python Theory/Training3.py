# Lesson --> Learning Dictionaries w/ One piece.

#String Variable are Devil Fruit Users.
captain = "Luffy"  #It gives only 1 box = 1 fact. Luffy Is the captain.

# Dictionaries is like the entire Straw Hat Crew Profile Card.

zoro = {
   "name": "Zoro",
   "role": "Luffy's Second Hand",
   "Combat Style": "Swordsman", # Previously missed a comma here, and the script broke.
   "Bounty": 1_111_000_000
}

print(zoro["name"])

# But wait, how are Dictionaries different from Lists? they're roles are similar. 1 box = Multiple Items.
# In essence... Lists are lineups and Dictionaries are databases.
# We use lists when order matters and we use Dictionaries when lookup by label matters. 

# For example let's compare them with an exercise to visualize the depth of the statement above...

# List.

straw_hats = ["Captain", "zoro", "usopp", "nami"]
print(straw_hats[2])

# Dictionary.

straw_hats = {
    "Captain": "Luffy",
    "2nd Hand of Captain": "Zoro",
    "Cook": "Sanji",
    "Navigator": "Nami",
    "Sniper": "Usopp",
    "Musician": "Brook",
} # Putting the print statement before this closing brace caused a syntax error.

print(straw_hats["Captain"])



