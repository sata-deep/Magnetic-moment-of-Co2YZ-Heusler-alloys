#This code calculates the M_SP for the Co2M1_(1-x)M2_xZ 
# Uses the standard definition:
# M_SP=N-24 (for Co2YZ compounds, N is the total number of valence electrons)
#Suppose if you are doing Co2Mn0.5Ni0.5Sb
# Please enter Mn Ni Sb 0.5
#Or  if you are doing Co2Fe0.75Ni0.25Sb
#Please use Fe Ni Sb 0.25

#Please note: Certain elements(Z) have underscore such for P it is P_



# Import math library
import math

# Prompt user for M1, M2, Z, and x
M1, M2, Z, x = input("Please provide M1, M2, Z, and x (separated by spaces): ").split()
x = float(x)

# Open and read the atom_features file
with open("atom_features", "r") as f:
    # Skip the header line
    next(f)
    
    # Initialize N1 and M_SP
    N1 = 0
    M_SP = 0
    
    # Loop through the lines in the file
    for line in f:
        # Split the line into the atom and feature columns
        atom, IE, XP, Rc, N, V, Nd = line.strip().split()
        
        # Check if the atom is M1, M2, or Z
        if atom == M1:
            N1 += (1 - x) * float(N)
            M_SP += (1 - x) * float(N) * (float(IE) - float(XP))
        elif atom == M2:
            N1 += x * float(N)
            M_SP += x * float(N) * (float(IE) - float(XP))
        elif atom == Z:
            N1 += float(N)
    
    # Subtract 6 from N1 to get the magnetic moment
    M = N1 - 6
    
    # Print the magnetic moment
    print("Slater-Pauling moment =", M)

