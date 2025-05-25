"""
File:    Pytzee.py
Author:  Sakar Ojha
Date:    10/29/2024
Section: 71
E-mail:  o66@umbc.edu
Description:
  Real game of Yathzee but with some exceptions
	"""
#----------------------------------------------------------------------------------------
import random
#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
TOTAL_DICE = 5
DICE_FACES = 6


# Upper section scoring types and scores of the scoreboard are recorded here in these lists
list_counts_types = ['count 1' , 'count 2', 'count 3', 'count 4', 'count 5', 'count 6']
list_count_scores = [0, 0, 0, 0, 0, 0]

# Lower section scoring types and scores of the scoreboard are recorded here in these lists
list_score_types = ['three of a kind','four of a kind','full house','small straight', 'large straight','yahtzee','chance']
list_scores = [0, 0, 0, 0, 0, 0, 0]

# All Types
all_types = ['count 1' , 'count 2', 'count 3', 'count 4', 'count 5', 'count 6', \
             'three of a kind','four of a kind','full house','small straight', 'large straight','yahtzee','chance']
#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
# Function will return random dice roll list (length of 5).
def roll_dice():
    """
    @return: random dice roll list (length of 5)
    """
    roll_list = []
    for i in range(5):
        random_number = random.randint(1,6)
        roll_list.append(random_number)

    return roll_list
#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
def print_dice(roll_list):
    for elements in roll_list:
        print(f'{elements}', end = '  ')
#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
# Function will take in random dice rolls and the user inputted count number, 
# then will add up all the count numbers in that roll and assigns the score to 
# the appropriate list index in  list_count_scores.
def count_section(random_list, count_value):
    
    score = 0
    for number in random_list:
        if number == count_value:
            score += count_value
    # Total score after adding all the sum of that value is then stored in the correct index of list_count_scores.        
    list_count_scores [count_value-1] = score
#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------\
def ordered_list(roll_list):
    ordered_list = []
    for element in roll_list:
        ordered_list.append(element)
    
    ordered_list.sort()

    return ordered_list
#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
# Chance Adds all the numbers of the roll_list 
def chance(roll_list):
    total = 0
    for element in roll_list:
        total += element
    
    return total
#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
# Function takes in the ordered list and then loops so that it starts from second index of the ordered list
# After which we can compare the second index to the first index and 
# if it matches we add 1 to variable match until it reaches 3.
def three_of_a_kind(ordered_list):
    match = 1
    for i in range(1, len(ordered_list)):
        if ordered_list[i] == ordered_list[i-1]:
            match += 1
            if match >= 3:
                return True
        else:
            match = 1
            
    return False
#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
# Same idea as three_of a kind function just that now match has change from >= 3 to >= 4
def four_of_a_kind(ordered_list):
    match = 1
    for i in range(1, len(ordered_list)):
        if ordered_list[i] == ordered_list[i-1]:
            match += 1
            if match >= 4:
                return True
        else:
            match = 1
            
    return False


#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
#Checks if the ordered list frome least to greatest is continuous for all 5 dices
def large_straight(ordered_list):

    first_index = ordered_list[0]

    for number in ordered_list:
        if number == first_index:
            first_index += 1

        else:
            return False
        
    return True
#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
# Sets variable continuous = 1 and loops through the ordered list 
# to make sure the index its checking is the last index + 1, returns true if continuous ever reaches 4.
def small_straight(ordered_list):

    continuous = 1

    for i in range(1, len(ordered_list)):
        if ordered_list [i] == ordered_list [i-1] + 1:
            continuous +=1 
            if continuous >= 4:
                return True
            
        elif ordered_list[i] != ordered_list[i-1]:
            continuous = 1

    return False
#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
# Sets pytzee variable to False and 
# if all the elements in the list don't match the first element, then returns false
def pytzee(roll_list):

    pytzee = False
    for element in roll_list:
        if element == roll_list[0]:
            pytzee = True
        else:
            return False
        
    return pytzee
#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
# three of a kind and a pair of a different type (for example, 4, 4, 4, 2, 2). 
# takes in ordered_list from asending order
def full_house(ordered_list):
    # If the first three are the same and the last two are the same
    if (ordered_list[0] == ordered_list[1] == ordered_list[2] and ordered_list[3] == ordered_list[4]):
        return True
    # If first 2 are the same and if the last three are the same
    elif (ordered_list[0] == ordered_list[1] and ordered_list[2] == ordered_list[3] == ordered_list[4]):
        return True
    else:
        return False
        
#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
def calc_total_score(list_scores , list_count_scores):
    total_score = sum(list_scores) + sum(list_count_scores)
    return total_score
#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
# FUnction that will be called in order to display the score card at with all the updated scores
def display_scorecard():
    print("Scorecard:")
    
    # Prints Upper Count Sections
    print("Upper Section:", end=' ')
    for i in range(len(list_counts_types)):
        print(f"{list_counts_types[i]}: {list_count_scores[i]}", end='  ')
    
    print()

    # Prints Lower Sections
    print("Lower Section:", end=' ')
    for i in range(len(list_score_types)):
        print(f"{list_score_types[i]}: {list_scores[i]}", end='  ')
    
    print()
#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
def play_game(num_rounds):
    for i in range(1, (num_rounds + 1)):
        print(f'***** Beginning Round {i} *****')
        print(f'Your score is: {calc_total_score(list_scores,list_count_scores)}')

        # Calling the random dice numbers and printing by passing into another function
        roll_list = roll_dice()
        print_dice(roll_list)
        print()

        # Users Choice
        users_choice = input('How would you like to count this dice roll? ').lower()

        # Ordered_list initialized, and If statements to determine the function to be called
        ordered_rolls = ordered_list(roll_list)

        # If user enters any other invalid inputs
        valid_input = False

        #while not((users_choice in list_counts_types) or (users_choice in list_score_types) or users_choice == 'skip'):
        # while not valid_input:
        #     if (users_choice in list_counts_types) or (users_choice in list_score_types) or (users_choice == 'skip'):
        #         valid_input = True

        while users_choice in all_types:

            
            #If user choice is not even something that makes sense 
            if not((users_choice in list_counts_types) or (users_choice in list_score_types) or (users_choice == 'skip')):
                print('That is not even a valid input. try again:', end = ' ')
            
            else:
                print('It already was entered. try again:', end = ' ')

            # We let the user type again
            users_choice = input()

            if users_choice in all_types:

                # Checks user choice and calculate scores accordingly
                if users_choice in list_counts_types:
                    # Gets the count value from user input
                    count_value = int(users_choice[-1])
                    count_section(roll_list, count_value)  
                    print(f'Scored {list_count_scores[count_value - 1]} for {users_choice}')

                # Three of a kind
                elif users_choice == "3 of a kind" or users_choice == "three of a kind":
                    if three_of_a_kind(ordered_rolls):
                        print("Three of a Kind!")
                        score = sum(ordered_rolls)
                        list_scores[0] = score
                        
                    else:
                        print("No Three of a Kind found.")

                # Four of a kind
                elif users_choice == "4 of a kind" or users_choice == "four of a kind":
                    if list_scores[1] == 0:
                        if four_of_a_kind(ordered_rolls):
                            print("Four of a Kind!")
                            score = sum(ordered_rolls)
                            list_scores[1] = score
                            
                        else:
                            print("No Four of a Kind found.")
                    else:
                        print('There was already a score in that slot.')

                # Full house
                elif users_choice == 'full house':
                    
                        if full_house(ordered_rolls):
                            print("Full House!")
                            score = 25  
                            list_scores[2] = score
                            
                        else:
                            print("No Full House found.")

                # Small straight
                elif users_choice == 'small straight':

                        if small_straight(ordered_rolls):
                            print("Small Straight!")
                            score = 30
                            list_scores[3] = score
                            
                        else:
                            print("No Small Straight found.")
                  

                # Large straight
                elif users_choice == 'large straight':
                    
                        if large_straight(ordered_rolls):
                            print("Large Straight!")
                            score = 40  
                            list_scores[4] = score
                            
                        else:
                            print("No Large Straight found.")
                   

                # Yahtzee
                elif users_choice == 'yahtzee':
                        if pytzee(roll_list):
                            print("Yahtzee!")
                            score = 50  
                            list_scores[5] = score
                            
                        else:
                            print("No Yahtzee found.")

                # Chance
                elif users_choice == 'chance':
                        print("Chance!")
                        score = chance(roll_list)
                        list_scores[6] = score

                # Removes the choice from the list all_types (remaining choices) after exiosting while loopp
                all_types.remove(users_choice) 
     
        # Displays the scorecard after each round
        display_scorecard()

# Calculates total score at the end
    total_score = sum(list_scores) + sum(list_count_scores) 
    print(f'\nGame over! Your final score is: {total_score}')
#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
# Beginning lines of the code where user is asked to enter round numbers and the seed value
if __name__ == '__main__':

    num_rounds = int(input('How many times do you want to play? '))

    if num_rounds > 0:
        seed = input('Enter the seed or 0 to skip: ')

        if seed != '0': 
            random.seed(int(seed))
            play_game(num_rounds)
    else:
        print("Please enter a valid number of rounds to play.")