#Lesson --> Combining Loops, Lists, Conditionals, Dictionaries, and Functions w/ Demon Slayer

# Toolbox.
    # Loops: for (1) [Item count dependent] and while (2) [Condition Dependent].
    # Lists (3), box with multiple items in it.
    # Dictionaries (4), stores in keys, and retrieved in key. [Different form of box storing multiple items]
    # Function (5), machine that conserves physics / equations for reusability.
    # Analogy --> Demon Slayer.

# Context... Tanjiro fights Muzan. 

# I want them to throw attacks to each other. Make them dodge erratically [dodge position driven by random indices within a range.],
# and develop new abilities during the combat. 

# Disclaimer... I do not read the manga, so I wont be able to define Muzan's nor Tanjiro's Strongest Combat Level, so I'll go with what the anime showcased so far.

import random # built-in random module imported for randomized calls on techniques, dodging positions, Strength stages, 
#environments [To account for the Tambourine Demon that helps muzan change surroundings]

# Define Tanjiro and Muzan's Fighting Styles with Dictionaries...
Tanjiro = { # How much damage each technique causes?
    "Water Breathing": { # Water Form, his trained fighting form. Since he has 10 forms of this trained style...
         # Could I define a list within a key in the dictionary? Yes!.... Corrected, Initially I used a list,
         # But I wanted to attach a damage count [Not an index, which is a mathematical position number to call values in a list.] 
         # to the style, so I "nested the dictionary" to have double keys. NEW CONCEPT].
        "First Form, Water Surface Slash!": 2500, # Damage.
         "Second Form, Water Wheel!": 3000,
         "Second Form, Lateral Water Wheel!": 3500,
         "Third Form, Flowing Dance!": 4000,
         "Fourth Form, Striking Tide!": 4500,
         "Fourth Form, Striking Tide, Turbulent!": 5000,
         "Fifth Form, Blessed Rain After the Drought!": 5500,
         "Sixth Form: Whirlpool!": 6000,
         "Seventh Form: Drop Ripple Thrust!": 6500,
         "Eighth Form: Waterfall Basin!": 7000,
         "Ninth Form: Splashing Water Flow!": 7500,
         "Tenth Form: Constant Flux!": 8000
    } , # Commas must be after curly bracket to follow up with the outer dictionary, and avoid syntax error.

    "Hinokami Kagura!": 10_500, # Sun Breathing, his innate fighting form.
    "Demon Slayer Mark lvl 1": 3000, # The red mark in his face. Upgrade lvl's by 3x.
    "Demon Slayer Mark lvl 2": 9000, # 
    "Demon Slayer Mark lvl 3": 27_000,
    "Forehead": 10000000,
    "Raw_sword_style": 900
}

# print(Tanjiro["Water Breathing"]["Second Form, Water Wheel"]) # To access a key I must use squared brackets... since it's nested, double that. [inner Dictionary.]
# print(Tanjiro["Hinokami Kagura"]) # Outer Dictionary.
# Both Inner and Outer dictionaries work properly, Cool!

random_technique = random.choice(list(Tanjiro["Water Breathing"])) # Random.choice, picks a random item from my dictionary, after converting keys into a list.
#This is the randomizer I'll need to call the Techniques during the fight.
# form = random.choice(list(Tanjiro["Water Breathing"]))
# print(form)

print(random_technique)

# random_technique_damage = Tanjiro[random_technique]

# print(random_technique,"=", random_technique_damage) 

# How could I call nested dictionary's keys?



Invisible_world = False # Defined Tanjiro's secret ability "Invisible World" learned in the Infinity Castle Part 1 to Maximize his dodging / fighting capability.


Muzan = { # Since I am unaware of how strong Muzan is and his abilities, I'll define his layers to be defeated.
    "Shapeshifting": "Camouflaged",
    "Blood Poisoning": "Poisoned", # Tanjiro's gets fatigued and his HP Decreases during the fight.
    "Absorption": { # Muzan eats one of these to increase his HP and strenght.
        "Akaza": { # Could I add double value?
            "HP": 6500,
            "Strength": 2000,
        },
        "Doma": {
            "HP": 9000,
            "Strength": 4500,
        },
    "Kokushibo": 10_000,
    }, 
    "Instant Regeneration": True # How could I enable this ability? Booleans are possible in Dictionary-Key-definition? They are.
} 

print(Muzan["Absorption"]["Akaza"]["HP"])

# Tatakae!
# note. Make Muzan Immune to some of Tanjiro's Techniques depending on which layer we are.
# note 2. Tanjiro will have to develop a new technique in the middle of the fight, to stand a chance against the Invincible & Nefarious Muzan.

# How can I call dictionary keys within a loop? To summon the randomized_keys during the fight.
# for form in Tanjiro.items():
#     print(form)


# Tanjiro_dodging = list(range(1,101)) # Dodging Positions.

# for dodge in range(len(Tanjiro_dodging)):
#     print(random.randint[dodge])




# def Combat (Tanjiro, Muzan):


# Where are they fighting? Let's go with the Inner most layer of the Infinity Castle's Labyrinth.







