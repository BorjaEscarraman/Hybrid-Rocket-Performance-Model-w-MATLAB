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

    if translation == Distance:
        print("The",Titan,"has arrived to", Wall,"outer edge")

# Define bool variables that activate Soldier's Efforts once the Titans arrive
#####

# Now let's define a function that represents the health [Fix = Damage Combination Polynomial] of the Abnormal,
# and what I plug are the Wing's of Liberty Soldiers attack damage.

Levi = 250 
Mikasa = 120 # HP
Erwin = 70 # HP
Abnormal_Health = 1000

#Abnormal_Health = 1000 #HP I mistakenly defined a variable with the name of the function, thinking it was a variable. No need for this!

def Abnormal_Remaining_HP (Abnormal_Health,Levi,Mikasa,Erwin):
    #Health = 1000 #Hidden Constant, non-reusable.
    total_damage = 2*Levi + 3*Mikasa + 2*Erwin
    remaining_health = Abnormal_Health - total_damage
    if remaining_health <= 0: # Finding the root here implies that we have killed the Titan. Satisfying the condition of Humankind's safety.
        print("It's Over")
        print("Wall Rose Has Been Saved from an Abnormal")
    return remaining_health

    # if Abnormal_Health == 0: This is my previous attempt where the conditional was incorrectly used.
    #     print("It's Over")
    # return -450*Levi + 240*Mikasa + 2*Erwin

print(Abnormal_Health(Levi,Mikasa,Erwin)) # This shows me what my function just computed.

 # Which is ridiculous, Levi Alone, could destroy thousands of these in minutes.
# Anyways good practice... [Issue : this prinnt is unconditional, so it will print no matter what.]


    
