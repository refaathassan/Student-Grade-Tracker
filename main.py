import numpy as np
grades=[]
try:
    for i in range(5):
        grades.append(int(input("enter the grade :  ")))
    print("the avarege grade is : ", np.sum(np.array(grades))/len(grades))
    with open("grades.txt","a") as file :
        file.write(str(grades))
        file.write("\n")
        file.close()
except ValueError as e :
    print("the exception is : ",e)
