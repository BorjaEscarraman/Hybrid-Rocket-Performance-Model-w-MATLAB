# Following through the all 27 Phases of Group 17, Launch 22nd in the Starlink Payloads sent w/ Falcon 9.

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
# 1 - LD Verifies Go for Propellant Load.
# The Launch director gives the 'action call' to start filling the Tanks wih Propellant [LOX & RP-1].
Robert_Plant_verf1 = True # Approves. # Disclaimer, LD's name is up to my discretion, NOT LEGIT. Led Zepellin Rocks...

if Robert_Plant_verf1: # Check once.
    print("Check 1 Successful.")
    print("Proceed to Check 2")

else:
    print("SHUTDOWN")

# 2 - Propellant Load begins.

LOX = 9000 #kg, Oxidizer.
RP_1 = 3500 #kg, Fuel.
Prop = LOX + RP_1 # Total mass in kg.
# Original is more like Falcon_wet_m = 549_060 # kg... includes both stages [dry mass, payload not included] and propellant [wet mass]. 
# To check that the Rocket is being loaded with my Propellant Mix, I'll assume my own Falcon 9 Dry Mass.
Falcon_dry_m = 3000
Falcon_wet_m = 3000
# Note. commas can't be used as they create tuples [ordered / immutable list.] Instead, I underscored it for readability. Is the same as 549060.

Loading = True
Full_capacity = False

while Loading and Full_capacity == False :
    print("Loading... Show increase in %...")
    Loading += 1 # Show increase in %'s until it reaches maximum capacity.





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

