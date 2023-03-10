from .Gradeable import *

#This class inherits from the Gradeable parent class and contains all the functions for calculating a student's GPA.
class Students(Gradeable):
    def __init__(self, data):
        super().__init__(data)

    #Calculates a student's grade average
    def student_average(self, student_id):
        grades = []
        for subject in self.data[student_id]["Grade"]:
            grades.append(self.data[student_id]["Grade"][subject])
        return self.get_average(grades)

    #Gets a letter grade for a student based on the grade
    def get_letter_grade(self, grade):
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
