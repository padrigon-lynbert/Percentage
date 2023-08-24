import os

def cls(): os.system('cls')
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
    
#=-----------------------------------------------------------------------------------------=>
def get_input():
    # global percentage, value_of_percentage, true_value
    # percentage, value_of_percentage, true_value = 0
    while True:
        while True:
            try:
                choice = float(input("What is missing?\n\n<1> Missing %\n<2> Missing value of %\n<3> Missing true value\n<4> Quit\n\n: ")); break   
            except ValueError: cls(); print("Invalid input. Please enter a valid number.")

        # if choice in range(1, 5): 
        #     if choice == 1:
        #         value_of_percentage = input("Value of percentage: ")

        cls()
        print("dfkjnd")
        

#=-----------------------------------------------------------------------------------------=>


def run(): pass
    # print(f"%: {look_for_percentage(value_of_percentage, true_value)}")
    # print(f"value of %: {look_for_value_of_percentage(percentage, true_value)}")
    # print(f"true value: {look_for_true_value(value_of_percentage, percentage)}")
    

# run()
get_input()