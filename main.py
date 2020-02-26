#!/usr/bin/python3
__author__      = "Travis Staehnke"
__description__ = "Calculate number of plates needed and type for barbell. (kg)"

'''
TODO
    - Menu in main.
    - Print inventory on start.
    - Sanitize data input for correctness.
'''

# Configure table for plate inventory.
from prettytable import PrettyTable
x = PrettyTable()
x.field_names = ["Plate (kg)", "Amount"]

print("Disclaimer: Plates range from 50kg -> 1.25kg. None of this twink 0.5kg crap.\n")

desired_weight = 19
bar = 19

inv_dict = {50:8, 25:2, 20:2, 15:2, 10:2, 5:2, 2.5:2, 1.25:2}

# Correctly input data
def get_data(text):
    temp = 1
    while temp % 2 != 0:
        temp = int(input("# of " + text + "kg = "))
        if temp % 2 != 0:
            print("Please enter multiples of 2 for pairs of plates.")
    return temp

# Loop input collection
def get_vars(desired_weight, bar, inv_dict):
    while (desired_weight % 5) != 0:
        print("Enter a bar weight that is a multiple of 5.")
        desired_weight = int(input("desired weight = "))

    while (bar % 5) != 0:        
        print("Enter a barbell weight that is a multiple of 5.")
        bar = int(input("empty barbell weight = "))
    
    

def inventory():
    print("*** Inventory ***")
    print("Empty barbell weight = ", bar, "kg")
    x.clear_rows() # Clear previous data
    x.add_row([50, inv_dict[50]])
    x.add_row([25, inv_dict[25]])
    x.add_row([20, inv_dict[20]])
    x.add_row([15, inv_dict[15]])
    x.add_row([10, inv_dict[10]])
    x.add_row([5, inv_dict[5]])
    x.add_row([2.5, inv_dict[2.5]])
    x.add_row([1.25, inv_dict[1.25]])
    print(x)


def main():
    get_vars(desired_weight, bar, inv_dict)
    inventory()

main()