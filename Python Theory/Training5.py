#Lesson --> Combining Loops, Lists, Conditionals, Dictionaries, and Functions w/ Demon Slayer

# Toolbox.
    # Loops: for (1) [Item count dependent] and while (2) [Condition Dependent].
    # Lists (3), box with multiple items in it.
    # Dictionaries (4), stores in keys, and retrieved in key. [Different form of box storing multiple items]
    # Function (5), machine that conserves physics / equations for reusability.
    # Analogy --> Demon Slayer.

# Environment... Tanjiro fights Muzan. I want them to throw attacks to each other. Make them dodge erratically, 
#[Positions driven by random indices within a list.]

# Dictionaries and lists are dominant...
Tanjiro = { # Define his fighting style Dictionary by how much damage each technique causes.
    "Water Breathing": { # Water Form, he's trained form. Since he has 10 forms of this trained style.
         # Could I define a list within a key in the dictionary? Yes! [Corrected, Initially a used a list,
         # But I wanted to attach a key [Not an index, which is a mathematical position number to call values in a list.] 
         # with a damage count, so I "nested the dictionary" which is a new concept for me.]
        "First Form, Water Surface Slash": 2500, # Damage.
         "Second Form, Water Wheel": 3000,
         "Second Form, Lateral Water Wheel": 3500,
         "Third Form, Flowing Dance": 4000,
         "Fourth Form, Striking Tide": 4500,
         "Fourth Form, Striking Tide, Turbulent": 5000,
         "Fifth Form, Blessed Rain After the Drought": 5500,
         "Sixth Form: Whirlpool": 6000,
         "Seventh Form: Drop Ripple Thrust": 6500,
         "Eighth Form: Waterfall Basin": 7000,
         "Ninth Form: Splashing Water Flow": 7500,
         "Tenth Form: Constant Flux": 8000,
    } , # Commas must be after curly bracket to follow up with the outer dictionary, and avoid syntax error.

    "Hinokami Kagura": 10_500, # Sun Breathing, he's innate form.
    "Demon Slayer Mark lvl 1": 3000, # The red mark in his face. Upgrade lvl's by 3x.
    "Demon Slayer Mark lvl 2": 9000, # 
    "Demon Slayer Mark lvl 3": 27_000,
    "Forehead": 10000000,
    "Raw_sword_style": 900
    
}

print(Tanjiro["Water Breathing"]["Second Form, Water Wheel"]) # To access the key I must use squared brackets... since it's nested, double that.

Invisible_world = False # Give tanjiro the ability to activate the Invisible World Ability learned in the Infinity Castle Part 1.

Muzan = { # Since I am unaware of how strong Muzan is and his abilities, I'll define his layers to be defeated.

}

# Tatakae Time!
#note. Make Muzan Immnue to some of Tanjiro's Techniques depending on which layer we are. On that account, Tanjiro
# will have to develop a new technique in the middle of the fight, give him a better chance.

# import random

# Tanjiro_dodging = list(range(1,101))

# for dodge in range(Tanjiro_dodging):
#     print(random.randint[dodge])


# def Combat (Tanjiro, Muzan):









