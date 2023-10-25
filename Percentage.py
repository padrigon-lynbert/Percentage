class Percentage: 
#calculate/algorithm for missing <function>
    def percentage(value_of_percentage, true_value):
        missing_percentage = (value_of_percentage/true_value) * 100
        
        return missing_percentage

    def value_of_percentage(percentage, true_value):
        missing_value = (percentage/100) * true_value

        return missing_value

    def true_value(value_of_percentage, percentage):
        missing_true_value = (value_of_percentage/percentage) * 100
        
        return missing_true_value
