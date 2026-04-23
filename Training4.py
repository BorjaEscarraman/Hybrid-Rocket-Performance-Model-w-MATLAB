# Lessons --> Learning about Functions w/ Attack on titan.

# In training 1, I introduced functions, and what they do... Today we'll go deeper on them.
# A function is a reusable machine... Where I assign the computation tools.

# Let's say I am the beast titan and I want to send Titans to destroy Wall Rose.

Titan = "Abnormal"
Distance = 100 # m. That's how far away he is from the Wall Rose.
Wall = "Rose" # Once he travels 100m, he will hit this target.

translation = 0 # Where the Titan is w.r.s.t the wall.

while translation < Distance:
    translation += 20
    print("Distance =", translation, "m" )

    if translation == 100:
        print("The",Titan,"has arrived to Rose's outer edge")

# Define bool variables that activate Soldier's Efforts once the Titans arrive
#####

# Now let's define a function that represents the health of the Abnormal,
# and what I plug are the Wing's of Liberty Soldiers attack damage.

Levi = -2 # HP
Mikasa = -3 # HP
Erwin = -90 # HP

Abnormal_Health = 1000 #HP

def Abnormal_Health (Levi,Mikasa,Erwin):
    result = -450*Levi + 240*Mikasa + 2*Erwin
    if result == 0:
        print("It's Over")
    return result

    # if Abnormal_Health == 0: This is my previous attempt where the conditional was incorrectly used.
    #     print("It's Over")
    # return -450*Levi + 240*Mikasa + 2*Erwin

print(Abnormal_Health(Levi,Mikasa,Erwin)) # This shows me what my function just computed.

print("Wall Rose Has Been Saved from an Abnormal") # Which is ridiculous, Levi Alone, could destroy thousands of these in minutes.
# Anyways good practice...


    