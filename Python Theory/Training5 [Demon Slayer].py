#Lesson --> Combining Loops, Lists, Conditionals, Dictionaries, and Functions w/ Demon Slayer

# Toolbox.
    # Loops: for (1) [Item count dependent] and while (2) [Condition Dependent].
    # Lists (3), box with multiple items in it.
    # Dictionaries (4), stores in keys, and retrieved in key, not in indices like lists. [Different form of box storing multiple items]
    # Function (5), machine that conserves physics / equations for reusability.
    # Context... Demon Slayer.

# Context... Tanjiro fights Muzan. 

# I want them to throw attacks to each other. Make them dodge erratically [dodge position driven by random indices within a range.],
# and develop new abilities during combat. 

# Disclaimer... I do not read the manga, so I wont be able to define Muzan's nor Tanjiro's Strongest Combat Level, so I'll go with what the anime
# showcased so far.

import random # built-in random module imported for randomized calls on techniques, dodging positions, 
#environments [To account for the Tambourine Demon that helps muzan change surroundings].

# Define Tanjiro and Muzan's Fighting Styles with Dictionaries...

# Tanjiro's Fighting Style.
Tanjiro = { # How much damage each technique causes?
    "Water Breathing": { # his trained Fighting Style. He has 10 forms of this style...
         # Could I define a list within a key in the dictionary? Yes!.... [Correction-->] Initially I used a list,
         # But I wanted to attach a damage count [Not an index, which is a mathematical position number to call values in a list.] 
         # to the style, so I needed to "nest the dictionary" to have double-binded keys, which it was a new concept for me].
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

    "Sun Breathing": { # his innate Fighting Style.
        "First Form: Dance!": 5000,
        "Second Form: Clear Blue Sky!": 6000,
        "Third Form: Raging Sun!": 7000,
        "Fifth Form: Fire Wheel!": 8000,
        "Sixth Form: Burning Bones, Summer Sun!": 9000,
        "Seventh Form: Sunflower Thrust!": 10_000,
        "Eighth Form: Sunflower Lance!": 11_000,
        "Ninth Form: Setting Sun Transformation!": 12_000,
        "Tenth Form: Raging Sun!": 13_000,
        "Eleventh Form: Fake Rainbow!": 14_000,
        "Twelfth Form: Flame Dance!": 15_000
    } , 
    #Later Stages.
    #"Demon Slayer Mark lvl 1": 3000, # The red mark in his face. Upgrade lvl's by 3x.
    #"Demon Slayer Mark lvl 2": 9000, # These are not breathing styles! Nest them.
    #"Demon Slayer Mark lvl 3": 27_000,
    "Forehead": 10000000, # When he has no energy he utilizes these (1)
    "Raw_sword_style": 900, # or this (2).
    "Invisible_world": False # Defined Tanjiro's secret ability "Invisible World" learned during Akaza's Fight in Infinity Castle Part 1 to maximize his dodging / fighting instinct.
}

# Testing how my dictionary works..
# print(Tanjiro["Water Breathing"]["Second Form, Water Wheel!"]) # To access a key I must use squared brackets... since it's nested, double that..
# print(Tanjiro["Sun Breathing"])
# Both Inner and Outer dictionaries work properly, Cool!

# How could I call nested dictionary's keys?
# How can I call the Water Breathing nested dictionary keys only when the random choice lands on the "Water Breathing" key? [Accomplished down below.]
breathing_style = random.choice(list(Tanjiro)) # Random.choice, picks a random item index-wise, which is why I had to convert Tanjiro's Dictionary into a list. This process is called "Materializing an iterable into a list."
# As I learn about using Libraries [Both Built-in and External] I pondered what is the source I must always go to, to see their module's potential.
    # With the goal of learning how to scan through documentation with Strategy.
        # For Built-in Libraries, use Python Doc... and use the search bar for rapid selection of module. [Python Doc has a Library Index Directory with all modules].
        # For External Libraries, use their official Documentation Website, where you'll see the Application Programming Interface (API), 
            # which is the set of rules and protocols to communicate and exchange info within the Script.
            #[New = Toggle Wrap with Alt + Z] and [Open Shortcut Assignment, Ctrl + K + S]

# print(breathing_style)

# [P. IMP = Pending Improvement {My own vocabulary}] Make this a function to call it during the fight!
if breathing_style == "Water Breathing":
    form = random.choice(list(Tanjiro["Water Breathing"])) 
    Damage = Tanjiro["Water Breathing"][form]

    # Calls out the Technique like the Character would do!
    # print(form, 'Damage =', Damage)

    # print(Damage)

elif breathing_style == "Sun Breathing":
    form = random.choice(list(Tanjiro["Sun Breathing"]))
    Damage = Tanjiro["Sun Breathing"][form]

    # print(form, 'Damage =', Damage)
    
elif breathing_style == "Forehead" or breathing_style == "Raw_sword_style":
    print("Tanjiro has No Energy...", breathing_style,'!', ) # [P. IMP] How could I represent the damage here?

# else: # [P. IMP] This command will fail because neither Muzan [Dictionary] nor his Demon Style is defined... I think functions will be the solution for calling both Tanjiro and Muzan at the same time.
#     print(Muzan)

#Muzan's Fighting Style.
Muzan = { # Since I am unaware of how strong Muzan is and his abilities... I'll have to improvise.
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

# Testing Muzan's dictionary...
# print(Muzan["Absorption"]["Akaza"]["HP"]) # The Nested Dictionary Works!

# Replicate Tanjiro's Fighting Style Randomizer on Muzan's.

Demon_Style = random.choice(list(Muzan))

# [P. IMP] Could Muzan and Tanjiro be functions? To compress the conditionals into a function, with temporary variables within? The only thing I care being 'permanent' is the dictionary.
# I have an issue, and is calling Muzan both name and abilities when is Tanjiro's turn. The reason that might be calling Muzan while it's Tanjiro's turn is because the only key of interest called is "Absorption".
def Muzan (Demon_Style):
    if Demon_Style == "Absorption":
            form = random.choice(list(Muzan["Absorption"]))
            Character = random.choice(list(Muzan["Akaza","Doma"]))
            Damage = Muzan["Absorption"][form][Character]

    return


##########
#Tatakae!#
###################################
# Make Tanjiro have the first hit.#
###################################


### Starting Health of Opponents.
Tanjiro_HP = 10_000
Muzan_HP = 90_000

### Randomizer for who attacks...
Muzan_vs_Tanjiro = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1] # Muzan == 0, Tanjiro == 1. # How Could I make this infinite? and with their names?
Attack_Selector = random.choice(Muzan_vs_Tanjiro)

if Attack_Selector == 1:
    print("TANJIRO! :", breathing_style, form, Damage) # [P. IMP] This command Fails sometimes, why?

elif Attack_Selector == 0:
    print("MUZAN! :", Demon_Style)

### Hit count per attack...

# def Combat (Tanjiro, Muzan):
#     tanjiro_attacks = false
        

# How can I call dictionary keys within a loop? To summon the randomized_keys during the fight.
# for form in Tanjiro.items():
#     print(form)


# Tanjiro_dodging = list(range(1,101)) # Dodging Positions.

# for dodge in range(len(Tanjiro_dodging)):
#     print(random.randint[dodge])


# def Combat (Tanjiro, Muzan):

# Where are they fighting? Let's go with the Inner most layer of the Infinity Castle's Labyrinth.
# note. Make Muzan Immune to some of Tanjiro's Techniques depending on which layer we are.
# note 2. Tanjiro will have to develop a new technique in the middle of the fight, to stand a chance against the Invincible & Nefarious Muzan.
