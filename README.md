# Magnetic-moment-of-Co2YZ-Heusler-alloys.
A general rule for predicting the magnetic moment of Cobalt-based Heusler compounds using compressed sensing and density functional theory.
This repository corresponds to the work:  

***Journal of Magnetism and Magnetic Materials 563 (2022) 169818***  
To calculate the general moment given by the formula:
![image](https://user-images.githubusercontent.com/27854932/232724701-ac4d3f50-8299-4521-9ce8-77d759c863ff.png)

one needs to calculate the magnetic moment via Slater-Pauling rule first for a Co2M1<sub>1-x</sub>M2<sub>x</sub>Z compound.   
1.This is done by issuing the command: python M_SP.py  
If you are doing for example: Co2Ti0.25Mn0.75 P. Then please run:  
**Please provide M1, M2, Z, and x (separated by spaces): Ti Mn P_ 0.75**  
the code will return the Salter-Pauling moment.  
2. Then run :python Nd.py to calculate the effective number of unoccupied d-electrons in the Y-site by  
**Please provide M1, M2, and x (separated by spaces): Ti Mn 0.75**  
It will return the Nd value.  
Now you are ready to calculate the the magnetic moment by the general rule  
3. Run M.py for that  
**Please enter M_SP: 5.25  
Please enter Nd for the Y site: 5.75  
The magnetic moment via general rule: 5.17**   
**<span style="color:red">Please check atom_feature file find out which elements require underscore (for example P is written as P_)</span>**  

Thats all.
