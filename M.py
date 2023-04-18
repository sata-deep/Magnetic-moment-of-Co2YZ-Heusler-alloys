#Once you have calculated the effective Nd and the 
# magnetic moment due to the Slater-Pauling rule please
#use this code.

import math

M_SP = float(input("Please enter M_SP: "))
Nd = float(input("Please enter Nd for the Y site: "))

# Calculate magnetic moment using the given formula
r = M_SP / Nd
M = Nd * (1 - math.exp(-r**3)) + M_SP * math.exp(-r)

# Print the magnetic moment
print("The magnetic moment via general rule:", M)

