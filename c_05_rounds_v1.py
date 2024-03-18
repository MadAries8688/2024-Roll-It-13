import random


# generates an integer between 0 and 6
# to simulate a roll of a die
def roll_die():
    result = random.randint(1, 6)
    return result


# rolls two dice and returns total and whether we
# had a double roll
    double_score = "no"

    # roll two dice
    roll_1 = roll_die()
    roll_2 = roll_die()

    # check if we have a double score opportunity
    if roll_1 == roll_2:
        double_score = "yes"

    # Find the total points (so far)
    first_points = roll_1 + roll_2

    # Show the user the result
    print("{who}: {roll_1} & {roll_2} - Total: {first_points}")

    return first_points, double_score


# Main routine starts here
print("press <enter> to enter this round: ")
input()

# Get initial dice rolls for user
user_first = two_rolls()
user-points = user_first[0]
# Tell the user if they are eligible for double points

# Get initial dice rolls for user

# Loop (while both user / computer have <= 13 points)`...
    # ask user if they want to roll again, update
    # points / status

    # Roll die for computer and update computer points
    
    # Outside loop - double user points if they won and are eligible

    # Show round results
