from Classes.Courses import *
from Classes.Students import *

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
        "First Name" : "Sam", 
        "Last Name" : "Hernandez",
        "Grade" : {
            "Physics" : 54,
            "History" : 94,
            "Geography" : 87
        }
    }
}

#This function opens and reads an excel file containing data.
def get_data(file_path, subject):
    data = {}
    file = open(file_path, "r")
    header = file.readline()
    for row in file:
        columns = row.split(",")
        data[columns[0]] = {
            "First Name" : columns[1],
            "Last Name" : columns[2],
            "Grade": {
                subject : float(columns[3])
            }
        }
    file.close()
    return data

#Testing with a csv file with grades from a math course.
data = get_data("Math_grades.csv", "Math")
math_course = Courses(data)
math_course.plot_grade_histogram("Math")