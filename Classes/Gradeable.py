#This is the parent class which contains all the statistical functions for anything that can be graded.
class Gradeable:
    def __init__(self, data):
        self.data = data
    
    #Calculates the average of a list of numbers
    def get_average(self, numbers):
        total = 0
        for num in numbers:
            total += num
        return float(total) / len(numbers)

    #Calculates the median of a list of numbers
    def get_median(self, numbers):
        numbers.sort()
        length_half = int(len(numbers) / 2)
        if len(numbers) % 2 != 0:
            return numbers[length_half]
        else:
            return ((numbers[length_half] + numbers[length_half - 1]) / 2)

    #Calculates the standard deviation of a list of numbers
    def get_stdev(self, numbers):
        average = self.get_average(numbers)
        sum_difference = 0
        for num in numbers:
            sum_difference += (num - average) ** 2
        return (sum_difference / len(numbers)) ** 0.5
