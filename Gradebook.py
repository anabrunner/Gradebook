import numpy as np
import matplotlib.pyplot as plt

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

#Calculates the median of a list of numbers
def get_median(numbers):
    numbers.sort()
    length_half = int(len(numbers) / 2)
    if len(numbers) % 2 != 0:
        return numbers[length_half]
    else:
        return ((numbers[length_half] + numbers[length_half - 1]) / 2)

#Calculates the standard deviation of a list of numbers
def get_stdev(numbers):
    average = get_average(numbers)
    sum_difference = 0
    for num in numbers:
        sum_difference += (num - average) ** 2
    return (sum_difference / len(numbers)) ** 0.5

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

#Plots a histogram of the class grades
def plot_grade_histogram(subject):
    grades = []
    for i in student_info:
        if subject in student_info[i]["Grade"].keys():
            grades.append(student_info[i]["Grade"][subject])
    plt.hist(grades, 10, (0,100))
    plt.xlabel("Grade")
    plt.ylabel("Number of students")
    plt.title("%s Grades" % str(subject))
    plt.figtext(0.01, 0.01, r'Avg. = %s, St. dev. = %s' % (str(round(get_average(grades), 1)), str(round(get_stdev(grades), 1))))
    plt.axis([0, 100, 0, 0])
    plt.autoscale(True, 'y')
    plt.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
    return plt.show()
