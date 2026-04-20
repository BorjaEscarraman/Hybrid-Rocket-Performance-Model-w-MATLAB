# 4 - 19 - 26.
# Lesson 1, installed 4 aerospace libraries...
    #  py -m pip install numpy scipy matplotlib jupyter
        # What this line verbally means...
        # Use Python to run pip, and tell pip to install 
        # these four packages into the current Python environment.
        # Python = Start Python.
        # -m = run module [file containing python code] inside python.
            # pip [Python's Package Installer] = the module.
        # Install = action for pip to do.
            # Name the libraries to be downloaded....
# The packages were accidentally installed in my Main Disk, not in this venv... 
    # Which could lead to potential issues when debugging, so I will re-install them.
    # Activated my current .venv = .venv\Scripts\activate
        # Verified location with = python -c "import sys; print(sys.executable)"
                                            #python -m pip --version
# Having Low-Storage in my Computer made me realize the difficulty in download .venv in a different folder from the projects.
# It gave me errors when I tried to install all of them at the same time since the path was too long!
    # However, it worked once I tried to install one by one. [DONE].


# Lesson 2, Lists // Indexing // Slicing.

# In Aerospace we deal with multiple variables during the analysis of systems...
# Single-valued Variables stop being enough when we have multiples: Temperatures, Pressures, Time steps...

# Variable is a box
Pressure = 30 # psi.


# List is a tray of boxes - Ordered collection of items.
Pressures = [30, 90, 40] # psi

    # Lists can mix data types.
Like = [True, "Frog", Pressure]
print(Like)

# Indexing (1), is the position [Left --> Right] of an item in the list.
print(Like[0]) # Zero in python is like 1.
print(Like[1])

# Inverse Indexing (2), '' '' [Left <-- Right] '' ''.
print(Like[-1]) # This is like zero, starting from the end.

# Slicing (3), grabbing a portion [A range of positions, not one like 'Indexing'].
# Where List implies = list[start:end]
#Pressures [0:1]
#print(Pressures)

Pressures [2] = 300 # Lists are modifiable...
print(Pressures)

# You can add values [Front or End].
Pressures.append(900) # End only.
print(Pressures)

Thrust = [200, 500, 1100]

Thrust.insert(1, 324) # Insert adds anywhere. list.insert (index, value)
print(Thrust)

# You can remove values
Thrust.pop(2) # Pop removes anywhere... list.pop (index)
print(Thrust)
Thrust.pop() # Empty index, removes automatically last value.
print(Thrust) 

# You can count the amount of items in a list with 'len'.
Thrust_readings = [300, 250, 200, 150, 100]
print(len(Thrust_readings))

# You can loop thru them... let's do both loop types;
# 1. For [Limited to item count] and 
# 2. While [Limited to condition].

#for Thrust in range(len(Thrust_readings)):
 #   print("Attack on titan Rocks!")

for Thrust in range(len(Thrust_readings)): # when using range, you must state position... range() will not list items... range(len(x)) or range(position) will work.
    print(Thrust, "=", Thrust_readings[Thrust]) # Prints both index and value.

# Now if I want to directly loop over the readings. NOT index = position of item.

for Thrust in Thrust_readings:
    print(Thrust)

# This variation goes through the readings (w/ Thrust index var.)

for Thrust in range(len(Thrust_readings)):
    print("Reading", Thrust, "=", Thrust_readings[Thrust])


# l = 0 # Count of items.


# while l < len(Thrust_readings): # While the count of items is less than the readings keep summing.
#     print("No Flight")
#     l = l + 1
    

# Which loop is the best option to deal with Lists?
    # 'for' loops, as they deal in autopilot through the list.
    # Unlike 'while' loops, that are useful, but more manual..
        # while loops are condition dominant.
        # for loops are list dominant.