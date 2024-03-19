'''
추가 문제 3번

Even if you haven’t studied physics (recently or ever!), you might have heard that 
e=mc^2, wherein e represents energy (measured in Joules), m represents mass (measured in kilograms), and c represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent.

In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.
'''

input_mass = int(input("mass(kg): "))
Joules = input_mass*(300000000**2)
print("Joules: ", Joules)
