from sage.all import *

# Change this value as needed
n = 7   # try 7, 8, 11, etc.

# Define the set Zn
R = Integers(n)

print("Set: Z_", n)

# Check Ring
if R.is_ring():
    print("It is a Ring")
else:
    print("It is NOT a Ring")

# Check Field
if R.is_field():
    print("It is a Field")
else:
    print("It is NOT a Field")

# Check Group (under addition)
# Zn under addition is always a group
print("It forms a Group under addition ✔")

# Extra: check if multiplicative inverses exist
print("\nChecking multiplicative inverses:")
for i in R:
    if i != 0:
        try:
            inv = i.inverse_of_unit()
            print(f"{i} inverse is {inv}")
        except:
            print(f"{i} has NO inverse")