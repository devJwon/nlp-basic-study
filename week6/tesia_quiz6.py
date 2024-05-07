#write a program that calculates BMI
#women: height * height * 21
#men: height * height * 22

def std_weight(height, gender):
    m_height = height /100

    if gender == "female":
        fem_weight = round(m_height * m_height * 21, 2)
        
        print("female of height {0}cm, weights {1}kg".format(height, fem_weight))
        
    else:
        male_weight = round(height * height * 22, 2)
        print("male of height {0}cm, weights {1}kg".format(height, male_weight))

std_weight(height = 179.5, gender = "male")
std_weight(height = 163.3, gender = "female")

