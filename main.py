import os #working in here _ not yet finished

def cls(): os.system('cls')
    # percentage = input("missing percentage: ")
    # value_of_percentage = input("missing value of percentage: ")
    
#calculate/algorithm for missing
def percentage(value_of_percentage, true_value):
    missing_percentage = (value_of_percentage/true_value) * 100
    
    return missing_percentage

def value_of_percentage(percentage, true_value):
    missing_value = (percentage/100) * true_value

    return missing_value

def true_value(value_of_percentage, percentage):
    missing_true_value = (value_of_percentage/percentage) * 100
    
    return missing_true_value
    
#=-----------------------------------------------------------------------------------------=> working here
def get_input():
    # global percentage, value_of_percentage, true_value
    # percentage, value_of_percentage, true_value = 0
    def get_percentage():
        while True: 
            try:
                value_of_percentage = float(input("Value of percentage: ")); break
            except ValueError: cls(); print("Invalid input. Please enter a valid number."); continue
     
        return value_of_percentage
    
    def get_true_value():
        while True: 
            try:
                true_value = float(input("True Value: ")); break
            except ValueError: cls(); print("Invalid input. Please enter a valid number."); continue
            
        return true_value
            
    def get_value_of_percentage():
        while True:
            try:
                value_of_percentage = float(input("Value of %: ")); break
            except ValueError: cls(); print("Invalid input. Please enter a valid number."); continue
            
        return value_of_percentage

    # while True:
    #     while True:
    #         try:
    #             choice = int(input("What is missing?\n\n<1> Missing %\n<2> Missing value of %\n<3> Missing true value\n<4> Quit\n\n: ")); break   
    #         except ValueError: cls(); print("Invalid input. Please enter a valid number.")

    #     if choice in range(1, 5):
    #         if choice == 1:
                
                    

    #     cls()
    #     print("dfkjnd")
        

#=-----------------------------------------------------------------------------------------=>


def run(): pass
    # print(f"%: {look_for_percentage(value_of_percentage, true_value)}")
    # print(f"value of %: {look_for_value_of_percentage(percentage, true_value)}")
    # print(f"true value: {look_for_true_value(value_of_percentage, percentage)}")
    

# run()
get_input()
