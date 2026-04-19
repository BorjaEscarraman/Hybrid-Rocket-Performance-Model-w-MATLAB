# Following through all 27 Phases of Group 17, Launch 22nd of the Starlink Payloads sent w/ Falcon 9.

# Source: all the checkpoints within the Falcon 9 Flight, 4/18/26, obtained through Next SpaceFlight.

# Vocab:
# LOX = liquid oxygen
# Prop load = propellant loading
# Strongback = pad support arm/tower structure
# Max-Q = peak aerodynamic loading
# MECO = main engine cutoff
# SES = second engine start
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

# 2 - Propellant Load begins.

# Define Propellant & Falcon 9 mass to check for successful loading.
LOX = 9000 #kg, Oxidizer.
RP_1 = 3500 #kg, Fuel.
Prop = LOX + RP_1 # Total mass in kg.
# Original is more like Falcon_wet_m = 549_060 # kg... includes both stages [dry mass, payload not included] and propellant [wet mass].
# Note. commas can't be used as they create tuples [ordered / immutable list.] Instead, I underscored it for readability. Is the same as 549060. 
# For simplicity, I'll assume my own Falcon 9 Dry Mass.
Falcon_dry_m = 3000 # Reference point to Start Loading mass Change.

#Define boolean based variables of the plumbing system that allows Propellant loading [True if Opened / False if Closed].
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

while percent < 95 and Loading < Full_capacity:
    step = random.randint(3,15)
    percent += step
    print("Loading %", percent) 
    print("Completed", percent) # How could I make it stop once % 100 in a print?
    Loading += step

    if percent > 100 and Loading == Full_capacity:
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





# 3 - LOX Chilldown - Falcon 9's Hardware is being adapted for cryogenic temperatures to maximize efficiency of LOX flow
# and avoid boil off due to contact of a possible warm metal [Causing issues like thermal shock, cavitation and unstable flow].


# LOX_T = (-340 - 32)/ 1.8 # Found Fahrenheit, Converted to Celsius [C].
# print(LOX_T)
#RP_1_T =


#LD Verifies Go for Launch.
# if Robert_Plant_verf1 and Robert_Plant_verf2:
# print ("Proceed for Ignition") 
# else:
    # print ("SHUTDOWN!")



# Launch Phase [#2] - Ignite and Punch through the Atmosphere.
# Staging Phase [#3] - Throw away dead weight. [First Stage Booster - Heavyweight figther against extreme aerodynamic loads].
# Orbital Phase [#4] - Upper Stage does the precision work.
# Recovery Phase [#5] - Upper Stage Booster comes home.
# Mission Phase [#6] - Satellites are released.

