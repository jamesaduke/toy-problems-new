# Link to problem
# https://www.hackerrank.com/challenges/grading/problem


def grading_students(grades):
    for i in range(len(grades)):
        if(grades[i]>37):
            if((grades[i]%5)!=0):
                if(5-(grades[i]%5)<3):
                    grades[i]+=5-(grades[i]%5)
    return (grades)
