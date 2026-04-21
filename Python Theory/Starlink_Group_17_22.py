from datetime import datetime # Show updated datetime on every log. Left 

print("Starlink Group 17-22,", datetime.now()) # Cleaner instead of datime.datetime.now()

# Following through all 27 Phases of Group 17, Launch 22nd of the Starlink Payloads sent w/ Falcon 9.

# Source: all the checkpoints within the Falcon 9 Flight, 4/18/26, obtained through Next SpaceFlight.

# Vocab:
# LOX = liquid oxygen
# Prop load = propellant loading
# Strongback = pad support arm/tower structure
# SECO = second engine cutoff
# Fairing = protective nose shell for payload

# Ground Phase [#1] - Fill the rocket, cool it, wake it up.
# 1 - LD Verifies Go for Propellant Load. ✓
# The Launch director gives the 'action call' to start filling the Tanks wih Propellant [LOX & RP-1].
Robert_Plant_verf1 = True # Approves. # Disclaimer, LD's name is up to my discretion, NOT LEGIT. Led Zepellin Rocks...

if Robert_Plant_verf1: # Check once.
    print("Check 1 Successful.")
    print("Proceed to Check 2")

else:
    print("SHUTDOWN")

# 2 - Propellant Load [Into the tanks]begins.

# Define Propellant & Falcon 9 mass to check for successful loading.
LOX = 9000 #kg, Oxidizer.
RP_1 = 3500 #kg, Fuel.
Prop = LOX + RP_1 # Total mass in kg.
# Original is more like Falcon_wet_m = 549_060 # kg... includes both stages [dry mass, payload not included] and propellant [wet mass].
# Note. commas can't be used as they create tuples [ordered / immutable list.] Instead, I underscored it for readability. Is the same as 549060. 
# For simplicity, I'll assume my own Falcon 9's Dry Mass.
Falcon_dry_m = 3000 # Reference point to Start Loading mass Change.

#Define boolean based variables of the plumbing system to allow Propellant loading [True if Opened / False if Closed].
Pumps = True
Valves = True
Throttles = True
#Plumbing_op = Pumps + Valves + Throttles # How could I make this variable work as a collector of all variables in a plumbing system
# But also work as a bool, in order to close it and open it as the loop [Line 58] comes to an end?

if Pumps and Valves and Throttles:
    print ("Path cleared to load!")

else:
    print ("Abort Propellant loading")

Loading = 0 # Falcon_dry_m starting point... Should I just let this be the dry mass?
Full_capacity = 15_500 # kg /s... AKA Falcon_wet_m.

import random

percent = 0

while percent < 90 and Loading < Full_capacity:
    step = random.randint(3,15) # What is this doing?
    percent += step
    print("Loading %", percent) 
#    print("Completed", percent) # How could I make it stop once % 100 in a print?

if percent > 90 and Full_capacity:
    percent = 100
    #Plumbing_op = False
    Pumps = False
    Valves = False
    Throttles = False
    print("Falcon 9 Fully Loaded with Propellant!")


#for Loading in range(3000, Full_capacity): # What kind of step should I do to show exponential growth to achieve a natural loading sequence, instead of a linear 1% , 2%, 3%...
    #print("Loading Initialized Show increase in %...")
    #Loading += 300 # Show delta % in increments until it reaches Full capacity. # Propellant variable, must be added in delay. Let the load increase exponentially.

    # if Loading < Full_capacity:
    #     print ("Loading")

    # elif Loading > Full_capacity:
    #     print("EXCESS ALERT!")

    # elif Loading == Full_capacity:
    #     print("Loading Completed")
    #     print("Proceed to Check 3")

# 3 - LOX Chilldown - Before the [Merlin] engines start... some of the LOX [Previously Loaded in the tanks] flows through the feed system and related hardware.
# With the goal of adapting Falcon 9's related hardware to cryogenic temperatures and maximize efficiency of LOX flow... as potential 
# warm metal/pipes/hardware could cause boil off the LOX. [and other issues like thermal shock, cavitation and unstable flow]. 
        #Imagine cooling a cup before throwing ice, to make it last longer.

LOX_T = (-297 - 32)/ 1.8 # Google gave Fahrenheit [F] LOX, so I converted to Celsius [C]. Conversion for "Operators" practice.
#print(LOX_T) #How do I control the amount of decimals shown?

# Quick lesson. [f-strings and decimals]
# First I'll have to understand what "f-strings" are... 
    # They build strings and insert variables directly inside them.
# How this differs from normal string variables? Well, 'normal strings' just store text, and 'f-strings' store both text and allow for value insertion.
        
        #name = "Borja"
        #print(f"Hello {name}") # the 'f' tells python this string may contain variables inside of the curly braces.

# x = 9.323121
# print(f"{x:.2f}") 
# (1) : starts format... (2) .2 = amount of digits shown after decimal... (3) f = completes the decimal full notation = [.2f].
# What's the difference between (), {} and [] in python?
#() groups things or call something. i.e. used for function calls, math grouping and tuples...
#[] ordered collection / grab position. i.e. used for lists, access indices, slicing...
#{} key-value data or special insert spots. i.e.. used for dictionaries, sets, f-strings inserts...


# Now is appropiate to allocate my LOX Converted output too...
print(f"{LOX_T:.1f}")


# Add Delay for LOX chilldown right after propellant is fully loaded into the tanks... Make it 5 seconds. Once it passes, the plumbing system allows the LOX flow.
# Let's make this a percentage of much of the LOX was used and how much it covered with that amount for the next. if > ...% follow to next stage... if < ..%
# Add Delay it 7 seconds until done. Then next phase.  



# 4 - 2nd Stage (S2) LOX load begins.


# 5 - Engine Chill
# 6 - Strongback retract
# 7 - 1st Stage LOX Loaded
# 8 - 2nd Stage LOX Loaded
# 9 - F9 In Startup
# 10 - TanK Press
# 11 - LD Go for Launch
        #LD Verifies Go for Launch.
        # if Robert_Plant_verf1 and Robert_Plant_verf2:
        # print ("Proceed for Ignition") 
        # else:
            # print ("SHUTDOWN!")

# Launch Phase [#2] - Ignite and Punch through the Atmosphere.

# 12 -  Engine Ignition # Time Delay for Countdown is crucial here.
# 13 -  Liffoff
# 14 -  Max-Q

# Staging Phase [#3] - Throw away dead weight. [First Stage Booster - Heavyweight figther against extreme aerodynamic loads].
# Max-Q = peak aerodynamic loading


# 15 - MECO
# MECO = main engine cutoff

# 16 - Stage Separation
# 17 - SES-1  
# SES = second engine start

# 18 - Fairing Separation
# 19 - 1st Stage Entry Burn
# 20 - 1st Stage Entry Burn Ends


# Orbital Phase [#4] - Upper Stage does the precision work.

# 21 - 1st Stage Burn Begins
# 22 - 1st Stage Landing  
# 23 - 2nd Stage Engine Cutoff (SECO-1)
# 24 - 2nd Stage Engine Start (SES-1)


# 25 - 2nd Stage Engine Cutoff (SECO-2)
# 26 - Starlink Deploy

# Recovery Phase [#5] - Upper Stage Booster comes home.
# Mission Phase [#6] - Satellites are released.

