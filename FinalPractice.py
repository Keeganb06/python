#!/usr/bin/env python3

#FinalPractice
#Keegan Brennan
#5/3/2021
#FinalPractice


class Die:
    def __init__(self,sides):
        self.sides=sides

#    @sides
#    def sides(self,sides):
      

    def roll_die(self,sides):
        if sides > 2:
            return randint(1,sides)
        else:
            print("Die must have at least 2 sides!")



def main():   

    # Make a 6-sided die, and show the results of 10 rolls.
    d6 = Die(6)


    results = []
    for roll_num in range(10):
        result = d6.roll_die(6)
        results.append(result)
    print("10 rolls of a 6-sided die:")
    print(results)

    # Make a 10-sided die, and show the results of 10 rolls.    d10 = Die(sides=10)

    results = []
    for roll_num in range(10):
        result = d10.roll_die()
        results.append(result)
    print("\n10 rolls of a 10-sided die:")
    print(results)

    # Test accessor, make a 20-sided die, and show the results of 10 rolls.
    d_new = Die(d10.sides + 10)

    results = []
    for roll_num in range(10):
        result = d_new.roll_die()
        results.append(result)
    print("\n10 rolls of a 20-sided die:")
    print(results)

    # Test mutator, make a 22-sided die, and show the results of 10 rolls.
    d_new.sides = 22

    results = []
    for roll_num in range(10):
        result = d_new.roll_die()
        results.append(result)
    print("\n10 rolls of a 22-sided die:")
    print(results)

    # Test exceptions
    # d = Die(0)  # uncomment to test
    # d_new.sides = 0 uncomment to test
# end main function

main()