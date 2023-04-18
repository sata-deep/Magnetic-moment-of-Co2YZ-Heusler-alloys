#This code calculates the effective number of unoccupied electrons 
# in the Y-site of the Co2YZ compound
#Suppose if you are doing Co2Mn0.5Ni0.5Sb
# Please enter Mn Ni 0.5
#Or  if you are doing Co2Fe0.75Ni0.25Sb
#Please use Fe Ni 0.25



M1, M2, x = input("Please provide M1, M2, and x (separated by spaces): ").split()
x = float(x)

# Open and read the atom_features file
with open("atom_features", "r") as f:
    # Skip the header line
    next(f)
    
    # Initialize Nd1
    Nd1 = 0
    
    # Loop through the lines in the file
    for line in f:
        # Split the line into the atom and feature columns
        atom, IE, XP, Rc, N, V, Nd = line.strip().split()
        
        # Check if the atom is M1 or M2
        if atom == M1:
            Nd1 += (1 - x) * float(Nd)
        elif atom == M2:
            Nd1 += x * float(Nd)
    
    # Print the calculated Nd1 value
    print("Nd1 =", Nd1)

