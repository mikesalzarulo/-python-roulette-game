#
# Michael Salzarulo
#
# Roulette.py
#
# A game where the user is told which color is assigned to the number they enter on the roulette wheel.
#
# Algorithm
# Input: A number (0-36)
# Processing: 1. Promt user for number (0-36)
#             2. Determine if number is between (0-36)  
#             3. Determine if number is 0 and green  
#             4. Determine if the number is red or black corresponding with the color on a roulette wheel
#             5. Display result.  
# Output: The color of the Wheel Pocket is (color)
#

# Define main function.
def main():
    # Intro.
    print('Roulette Wheel Colors App ...')
    # Prompts user for a random whole number between 0 and 36.
    num = float(int(input('Please enter pocket number (0-36):')))

    # Tests if input is within color wheel range.
    if num >= 0 and num <= 36:

        # Print pocket is green if 0.
        if num == 0:
            print('Pocket 0 is green.')

        # Print pocket is black if (1-10 and even).
        elif (num >= 1 or num <= 10) and num % 2 == 0:
            print('The color of the Wheel Pocket is Black')

        # Print pocket is red if (1-10 and odd).
        elif (num >= 1 or num <= 10) and num % 2 != 0:
            print('The color of the Wheel Pocket is Red')

        # Print pocket is red if (11-18 and even).
        elif (num >= 11 or num <= 18) and num % 2 == 0:
            print('The color of the Wheel Pocket is Red')

        # Print pocket is black if (11-18 and odd).
        elif (num >= 11 or num <= 18) and num % 2 != 0:
            print('The color of the Wheel Pocket is Black')

        # Print pocket is black if (19-28 and even).
        elif (num >= 19 or num <= 28) and num % 2 == 0:
            print('The color of the Wheel Pocket is Black')

        # Print pocket is red if (19-28 and odd).
        elif (num >= 19 or num <= 28) and num % 2 != 0:
            print('The color of the Wheel Pocket is Red')

        # Print pocket is red if (29-36 and even).
        elif (num >= 29 or num <= 36) and num % 2 == 0:
            print('The color of the Wheel Pocket is Red')

        # Print pocket is black if (29-36 and odd).
        elif (num >= 29 or num <= 36) and num % 2 != 0:
            print('The color of the Wheel Pocket is Black')

        # Prints error if input is not in range.
        else:
            print('Error ... Invalid pocket. Try Again')

    # Prints error if input is not in range.        
    else:
        print('Error ... Invalid pocket. Try Again')
main()
