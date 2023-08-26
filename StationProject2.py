import random


def roll_dice():
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    print(f"The sum of dice is {a} + {b} = {a + b}")
    return a + b


def game():
    input("Press Enter to roll the dice...")
    first_roll = roll_dice()

    if first_roll in [7, 11]:
        return "You won!"
    elif first_roll in [2, 3, 12]:
        return "You lose."

    goal = first_roll
    
    print(f"Goal is {goal}")

    while True:
        input("")
        current_roll = roll_dice()

        if current_roll == 7:
            return "You lose."
        elif current_roll == goal:
            return "You won!"



if __name__ == '__main__':
    print(game())


