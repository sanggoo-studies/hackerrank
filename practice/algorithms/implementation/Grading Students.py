#
# Complete the gradingStudents function below.
#


def gradingStudents(grades):
    for i in range(len(grades)):
        mul = grades[i] + 5 - (grades[i] % 5)
        if mul - grades[i] < 3 and mul >= 40:
            grades[i] = mul
    return grades


print(gradingStudents([73, 67, 38, 33]))
