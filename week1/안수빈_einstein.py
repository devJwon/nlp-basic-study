'''
추가 문제 3번

Even if you haven’t studied physics (recently or ever!), you might have heard that 
e=mc^2, wherein e represents energy (measured in Joules), m represents mass (measured in kilograms), and c represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent.

In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.
'''

mass_input = int(input("질량을 킬로그램 단위로 입력해 주세요: "))

light = 300000000
energy_1 = mass_input * (light ** 2)
energy_2 = mass_input * light ** 2


print(str(mass_input) + "kg의 에너지는 " + str(energy_1) + "줄입니다.")
print(str(mass_input) + "kg의 에너지는 " + str(energy_2) + "줄입니다.")ㅏ
