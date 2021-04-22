# Evelina Ramoskaite
# Towers of Hanoi

# There are 3 posts
# One post has a tower of disks
# The goal is to move the stack to a new tower
# Base case - moving only 1 disk to another tower

##### Rules#####
# Only the top disk from a stack can be removed
# A large disk cannot go over a small disk



def hanoi(n,source,target,spare):
    """Moves n disks from the source to the target, using spare as an auxiliary rod"""
    # Recursion base case
    if n ==1:
        print(f"Move disk from {source} ==> {target}")
        return

    # Move disks from the source to the spare tower.
    hanoi(n-1,source,spare,target)
    print(f"Move disk from {source} ==> {target}")

    # move the remaining disks from the spare to the target.
    hanoi(n-1,spare,target,source)




# Running Hanoi for situations with 1-4 disks
Source = 'A'      # Assigning tower names
Target = 'C'
Spare = 'B'

for n in range(1,5):    # Calling the Hanoi function for each scenario
    print("---------------------------------------------------------\n")
    print(f"Hanoi {n}\n")
    print(f"Moving {n} disks from tower {Source} to tower {Target}:")
    hanoi(n,Source,Target,Spare)
    print("NIL")

