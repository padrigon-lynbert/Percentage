

def get_input():
    global percentage, value_of_percentage, true_value
    while True:
        while True:
            choice = input("What is missing?\n\n<1> Missing %\n<2> Missing value of %\n<3> Missing true value\n<4> Quit")
            if choice in range(1, 5): break



    # percentage = input("missing percentage: ")
    # value_of_percentage = input("missing value of percentage: ")
    

def look_for_percentage(value_of_percentage, true_value):
    missing_percentage = (value_of_percentage/true_value) * 100
    
    return missing_percentage

def look_for_value_of_percentage(percentage, true_value):
    missing_value = (percentage/100) * true_value

    return missing_value

def look_for_true_value(value_of_percentage, percentage):
    missing_true_value = (value_of_percentage/percentage) * 100

def run():
    print(f"%: {look_for_percentage(value_of_percentage, true_value)}")
    print(f"value of %: {look_for_value_of_percentage(percentage, true_value)}")
    print(f"true value: {look_for_true_value(value_of_percentage, percentage)}")
    

run()