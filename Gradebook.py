#Some test data while building the functions. Each student has an unique student ID in case their name is not unique.
student_info = {
    1 : {
        "First Name" : "Alice", 
        "Last Name" : "Smith",
        "Grade" : {
            "Math" : 80,
            "Chemistry" : 74,
            "Physics" : 86
        }
    },
    2 : {
        "First Name" : "Bob", 
        "Last Name" : "Wang",
        "Grade" : {
            "Art" : 91,
            "Physics" : 73,
            "Math" : 59
        }
    },
    3 : {
        "Name" : "Sam", 
        "Last Name" : "Hernandez",
        "Grade" : {
            "Physics" : 54,
            "History" : 94,
            "Geography" : 87
        }
    }
}

#Calculates the average of a list of numbers
def get_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return float(total) / len(numbers)

#Calculates a student's grade average
def student_average(student_id):
    grades = []
    for subject in student_info[student_id]["Grade"]:
        grades.append(student_info[student_id]["Grade"][subject])
    return get_average(grades)

#Gets a letter grade for a student based on the grade
def get_letter_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"

#Calculates the class average for a specific subject
def class_average(subject):
    grades = []
    for i in student_info:
        if subject in student_info[i]["Grade"].keys():
            grades.append(student_info[i]["Grade"][subject])
    return get_average(grades)
