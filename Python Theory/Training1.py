#Set virtual environment (venv). 
#Why do I need this? Selecting the interpreter and setting the environment is like preheating the oven before cooking.
    # Project / code is the meal.
    # Python Interpreter is the oven.
    # Virtual Environnment is the oven setup.
    # Packages / librariesare the ingredients and tools place in position for usage.

# if not set correctly, the meal [Project] may not turn out as desired. raw or burnt, etc.

#Python is a small control room... Doing 3 things.
# 1. Store Info.
# 2. Change Info.
# 3. Decisions based on the Info.

# The smart correction is bothering me...  Open settings [Ctrl + ,]. Fixed! it was the Copilot Inline suggestion.
# Ctrl plus + / - zoom out / in.
# Copilot for quick assistance in questions.. Ctrl + alt + I
# When the file is "yellow" is due to unknown variable identification or because it has unsaved changes.

# 6 Basics for today...
# Variables [1], a box that stores values. A !must! to store engineering quantites like velocity, pressure, density, temperature...
# Now, there's various ~Data types~ [2] since not every box stores the same kind of thing, like;

    #int [Integers - whole numbers/negative/zero] 
A = 10 # m^2 # note. = sign is not "equals" in math sense, it binds box [left] w/ value [right].
v_avg = 16  # m/s, # note, comments can be used for unit track.
rho = 9 # kg / m^3
g = -9.81 # m/s^2

    #float [Real numbers - fractions/decimals/repeating/continuous]
phi = 2*3.14/3.14 * 180
# So on... Defining variable variables for decision making and changes alogn the script []

    #str [Words]

BSAE_student = "Brailer" # Don't mix numbers w/ strings, this will always present a !text!, never a number quantification.

    #bool [True or False -- ON or OFF]

engine_on = False
engine_off = True
#-----------------------------------------------------------------------------------------------------------------------------------
# Operators [3], value combinator / manipulator. [Simple math arithmetic definition... combining / manipulating values w/ operators].
# I'll use this for formulas, scaling, ratios, exponents and unit conversions.

#Using previously defined int values [Thermodynamics concept... Mass Flow Rate.]

m_dot1 = rho + A + v_avg # Addition
m_dot2 = rho - A - v_avg # Substraction
m_dot5 = rho*A*v_avg # Multiplication # Correct usage!

# Redistributing the variables to find density by division.
m_dot6 = 8 # kg/s.
rho = m_dot6/A*v_avg # AHA! There's a mistake here. I can't just redistribute if rho is already defined, 
#how do I neglect my current value of rho to properly isolate? For now this will stay as it is.
m_dot7 = 10 ** 2 # Power.
m_dot8 = 10 % 3 #  This is one always gets me confused so; 
#Quotient = how many times the divisor [3] fits in the dividend [10] completely... 
#Remainder = what's left over. i.e. theres 3, 3's inside of 10, and for completion add 1 as the crumb. Never count the decimal. 

#Example.
velocity = 3
mass = 2

KE = velocity * mass

# Additional... Operators can be separated into 3 subcategories.
    #Arithmetic = +, - , *, /, //, %, **
    #Comparison = >, <, <=, >=, ==, !=
    #Logic = and or not.

#-----------------------------------------------------------------------------------------------------------------------------------
# Conditionals [4] [Conditions function as thresholds (limits), as it defines a specific point / boundary, where the process shifts it's state.]

# For example, As my Rocket Launches... it's altitude / mass / loads / temperatures and a bunch of other parameters are constantly changing, hence, with conditions,
# you signal the system to change parameter readings once it reaches a certain altidude / loss of mass / thermal load / pressure, or whatever you want.

# Theres 3 main types of conditions; if, elif, else... for control flow

# if (1) is a one-time decision maker, whether it fails or succeeds.
# For example, as I want to gage how much I can rely on my propellant's Mixture Ratio [O/F, i.e. 4 : 1, is read as 4 to 1 ratio or 4kg of Oxygen for every 1 kg of Fuel]
# for my Rocket, I will do the following...
O = 5 # kg 
F = 2 # kg
T1 = 290 # deg
T2 = 390 # deg
T3 = 490 # deg

#note. we use the colon in a code block to open a gate; everything indented after it, belongs to that conditional block.
if O > F and T3 > 500: # Since O is greater than F, the if statement is approved and it prints the value below... Don't forget the colon!
    print("O/F test passed") # which is appropiate in Rocket Science, since Oxidizers have to be significantly greater by mass than fuel for complete combustion.
    # Indentation is needed to provide structure
elif T1 > 300: # note 1. elif (2) next special condition  # note 2. elif and if must be in the same level of indentation as they're siblings.
    print("Too cold to combust")

elif T2 > 400:
    print("Warmer, but not enough")

elif T3 > 500:
    print("Almost there!")

else: # else (3) occurs as the default option if all the previous conditions fail.
    print("O/F is appropiate")
    print("Ready for efficient combustion")

# This how you build, safety margins, model logic, warning systems, regime changes, etc...


#-----------------------------------------------------------------------------------------------------------------------------------
# Loops [5] is the procedural decision maker, where the amount of iterations depends on a !stopping command! or in the !amount of items! to sequence through.

# There a 2 main types of loops, 'for' and 'while'... for repeated machine instruction control.

#note. just learned that you can wrap a text in symbols when selected and clicked '' or ""... like "Pig" with Ctrl + /.
#Let's work with 'De laval Nozzle' Conditions. Used in Rocketry, to interpret the subsonic, transonic and supersonic regions within a commonly used Rocket Nozzles.

Combustion_cha_v = 300 # m/s Starting point after 'Injector' sprays the jets of propellant [atomization] for efficienct mixing and combustion.
Converging_v = 600 # m/s, inlet
Throat_v = 1235 # m/s, choking section
Diverging_v = 2000 # m/s, after throat
exhaust_v = 3235 # m/s outlet
# as you notice the velocity increases since the functionality of a nozzle is to convert enthalpy to kinetic energy, and hence, increase velocity. Is choking the propellant of 
# any use to accelerate the propellant too? Choking locks the flow rate at Mach 1, so it becomes a limiting transition point, that incites an easier path to reach supersonic state.
# note. you can force a text into a comment with Ctrl + /.

# Since we know the collection or number in repeat, we use for loops (1).

#for i in range(Combustion_cha_v,Converging_v,1): # Means that it starts at "Combustion_cha_v", ends at "Converging_v", in steps of "1". 
#   print(i)

#for l in range(Converging_v): #If we only state 1 variable, it will count up to the number. excluding the limit and always starting from "ZERO"
#    print(l)

# I believe is appropiate to define 'lists,' they are containers that contain multiple amount of variables [all data types]... mathematically called an array.
# It's convenient to define lists to create a range [In case I want to pick a certain position / index] for the loop, as well as avoiding having loose variables. 
# Ultimately, having an outcome that makes sense more than just controlling 1 variable, which is not true in real scenarios.

nozzle_vel = [Combustion_cha_v, Converging_v, Throat_v, Diverging_v, exhaust_v] # Clean receptacle!

#Say that... for i in range(nozzle_vel). where 'i' is the index / entry allocator within the range, and 'range' chains our box capacity with the loop.
#Since 'i' is a placeholder, you can name it anything, so i'll take in an appropiate name to it.

#for speed in range(nozzle_vel):
#    print(speed)
# this will be an error since the current range is interpreted as an integer, but is a list.
# instead we use 'len' which takes in all variables within the list.

#for speed in range(len(nozzle_vel)): # now it names the amount of entries in my list, and it doesn't count up to the number
#    print(speed)


# When an iteration requires depending on a condition, meaning that it will only start or end once those conditions are initially approved and put to an end, it's considered a 
# While loop (2)

feed_sys_v = 5 # m / s
injector_v = 10 # m / s

before_nozzle_v = [feed_sys_v, injector_v]

#while before_nozzle_v < nozzle_vel: # List section
#    print("Rocket Flow Sequence is reliable")

#note. the flaw in the code above was comparing differently sized lists... hence is appropiate to add iteration thresholds instead of using the lists.

iterations = 0
max_iterations = 5

#while iterations < max_iterations:
#  print("Rocket Flow Sequence is reliable")
#    if Diverging_v > exhaust_v: # Integer section. # note. NEVER combine lists and integers
#        print("Flow sequence became unstable!")
#        iterations += 1
#    else:
#        print("Flow sequence is stable")
#    break

#note. breaking the code is too easy. Instead, i'll manipulate the loops with bool variables.

# is_reliable = True

# while is_reliable: # For now... I am not very proud of the logic outcome on this loop. But I need to move on.
    # print("Rocket Flow Sequence is reliable")
    # iterations += 1

    # if Diverging_v < exhaust_v:
    #     print("Flow sequence became unstable!")
    #     is_reliable = False

    

# Used to step through data, repeat calcs, time marching, iterative solvers, convergence checks [residuals, stability, accuracy, time-independence].

#-----------------------------------------------------------------------------------------------------------------------------------
# Functions [6], is a reusable machine that can utilize packages [variables] assigned to it. They define the calculation tools. [thrust, efficiency, etc.]

#In MATLAB, functions are pure definitions, meaning that they can be either at the top or bottom... Python's different, is a sequential execution model, 
# meaning that functions aren't location-independent. Hence, its strictly read sequentially from top to bottom, 

#Like a recipe. # Variables [Ingredients] and Functions [Technology to cook it] are usually written in the beginning of a script
#def square(x): # def = define. This names the function.
#    return x ** 2 # What it sends back out. 'x' is the material fed into the system.

#result = square(4)
#print(result)

# note. in case you want to change name of 1 variable that is repeated multiple times... select the variable, then, Ctrl + D.

#In pre-calculus,
#def: Defines 'y' function (the "machine").
#return: Plugs in the x values and computes the result.
#result: Stores the output y(x) = ... after evaluation.

x = 3 #Variable to be used in my machine [function].

def y(x): # Defining y... function.
    return x*2 # Plugging x into y.

result = y(x) # Store result.
print(result) # Show result.


# In Python,
# 'def' defines the tool... with a name to apply inputs [Coming from the variables].
# 'return' send result back... Functions defined are like black boxes, they take inputs, return outputs. Like a factory sending finished products.
# 'answer' stores the output for further use.

# Let's define variables based on the thrust function [Equation Extracted from NASA Glenn Research Center]...

# Always define variables [Food] before the function [Cookie Monster].
m_dot = 34 # kg / s
V_e = 34
V_0 = 20
A_e = 50
p_e = 10
p_0 = 30

def thrust(m_dot, V_e, V_0, A_e, p_e, p_0): # Define tool. Also, make sure all the variables are addresses in the return equation [variables go from dim to bright].
    return m_dot*V_e - m_dot*V_0 + A_e*(p_e - p_0) # Plug variables [x] into thrust [y].

answer = thrust(m_dot, V_e, V_0, A_e, p_e, p_0) # Store result.
print(answer) # Show result.

# Same idea both in Calculus and Python computed correctly!

# That's all the basics!



