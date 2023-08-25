import os #my very own module about percentages (very basic but it was fun to coding this)

def cls(): os.system('cls')
    
class Percentage: 
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
    
# #uncomment below to run it by itself     
# def get_input():
#     def get_percentage():
#         while True: 
#             try:
#                 percentage = float(input("Percentage: ")); break
#             except ValueError: cls(); print("Invalid input. Please enter a valid number."); continue
     
#         return percentage
    
#     def get_true_value():
#         while True: 
#             try:
#                 true_value = float(input("True Value: ")); break
#             except ValueError: cls(); print("Invalid input. Please enter a valid number."); continue
            
#         return true_value
            
#     def get_value_of_percentage():
#         while True:
#             try:
#                 value_of_percentage = float(input("Value of %: ")); break
#             except ValueError: cls(); print("Invalid input. Please enter a valid number."); continue
            
#         return value_of_percentage

#     while True:
#         cls()
#         while True:
#             cls()
#             try:
#                 choice = int(input("What is missing?\n\n<1> Missing %\n<2> Missing value of %\n<3> Missing true value\n<4> Quit\n\n: ")); break   
#             except ValueError: cls(); print("Invalid input. Please enter a valid number.")

#         if choice in range(1, 5):
#             if choice == 1: print(f"{round(Percentage.percentage(get_value_of_percentage(), get_true_value()), 2)}%")
#             elif choice == 2: print(f"% = {round(Percentage.value_of_percentage(get_percentage(), get_true_value()), 2)}")
#             elif choice == 3: print(f"True vvalue = {Percentage.true_value(get_value_of_percentage(), get_percentage())}")
#             else: cls(); quit()
#         input("\n\n<ENTER>\n\n")

# def run():
#    get_input()
   
# run()

