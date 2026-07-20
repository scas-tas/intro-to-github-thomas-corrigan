"""
Context
You are writing software for a delivery company that dispatches five trucks each morning. Each truck is loaded with a number of packages before it heads out.
Sometimes two trucks need to be combined onto one route -- for example, if a truck breaks down, or two nearby routes get merged to save fuel. 
Before dispatch can approve this, they need to know the total number of packages the combined trucks would carry.
You'll write a function that takes the list of package counts and two truck numbers, and returns the total packages across those two trucks.
Note: trucks are numbered 1-5 (truck 1 is the first truck), but Python lists are indexed from 0. You'll need to convert between the two.
"""


def combine_trucks(trucks, first_truck, second_truck):
    # TODO: return the total packages in first_truck and second_truck
    
    pass



def main():
    trucks = [4, 7, 2, 6, 9]
    print(combine_trucks(trucks, 2, 4))  # Expected: 13
    print(combine_trucks(trucks, 1, 3))  # Expected: 6


main()
