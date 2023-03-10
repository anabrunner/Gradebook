from .Gradeable import *
import numpy as np
import matplotlib.pyplot as plt

#This class inherits from the Gradeable parent class and contains all the functions for calculating and plotting course statistics for a specific subject.
class Courses(Gradeable):
    def __init__(self, data):
        super().__init__(data)
    
    #Calculates the class average for a specific subject
    def class_average(self, subject):
        grades = []
        for i in self.data:
            if subject in self.data[i]["Grade"].keys():
                grades.append(self.data[i]["Grade"][subject])
        return self.get_average(grades)

    #Plots a histogram of the class grades
    def plot_grade_histogram(self, subject):
        grades = []
        for i in self.data:
            if subject in self.data[i]["Grade"].keys():
                grades.append(self.data[i]["Grade"][subject])
        plt.hist(grades, 10, (0, 100))
        plt.xlabel("Grade")
        plt.ylabel("Number of students")
        plt.title("%s Grades" % str(subject))
        plt.figtext(0.01, 0.01, r'Avg. = %s, St. dev. = %s' % (str(round(self.get_average(grades), 1)), str(round(self.get_stdev(grades), 1))))
        plt.axis([0, 100, 0, 0])
        plt.autoscale(True, 'y')
        plt.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
        return plt.show()
