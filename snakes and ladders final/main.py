#importing all the required modules
import time
import random
import sys


# function for printing the text for player turn
text_for_plr_turn = [
    "It's your turn. Hit enter to roll the dice.",
    "Are you prepared?",
    "Let's go.",
    "Please move along.",
    "You are doing great.",
    "Ready to be a champion.",
    "",
]

# function for printing the text for snake bite
text_for_snake_bite = [
    "Boom!",
    "Bang!",
    "Snake bite!",
    "Oops!",
    "Dang",
    "Oh no!",
    "Alas!"
]

# function for printing the text for ladder jump
text_for_ladder_jump = [
    "Yipee!",
    "Wahoo!",
    "Hurrah!",
    "Oh my goodness...",
    "You are on fire!",
    "You are a champion!",
    "You are going to win this!"
]

# Dictionary containing snake bite positions

# Snake Positions where key is the head of snake and value is the tail of snake
snake_position = {
    12: 4,
    18: 6,
    22: 11,
    36: 7,
    42: 8,
    53: 31,
    67: 36,
    73: 28,
    80: 41,
    84: 53,
    90: 48,
    94: 65,
    96: 80,
    99: 2
}

# Ladder Positions where key is the bottom of ladder and value is the top of ladder
ladders_position = {
    3: 26,
    5: 15,
    13: 44,
    25: 51,
    29: 74,
    36: 57,
    42: 72,
    49: 86,
    57: 76,
    61: 93,
    77: 86,
    81: 98,
    88: 91
}

# Function for printing the rules of the game
def first_msg():
    msg = """Welcome to the Snake and Ladder game!
    Rules:
    - The game is played by two players.
    - Each player takes turns to roll the dice and move their position accordingly.
    - If a player lands on the head of a snake, they go down to the tail.
    - If a player lands at the bottom of a ladder, they climb up to the top.
    - The first player to reach or exceed 100 wins the game.
    """
    print(msg)

# Delay of 1 second between each action
SLEEP_BETWEEN_ACTIONS = 1
MAX_VAL = 100
DICE_FACE = 6

# Function to get player names
def get_player_names():
    p1_name = None
    while not p1_name:
        p1_name = input("Name of the first player: ").strip()

    p2_name = None
    while not p2_name:
        p2_name = input("Name of the second player: ").strip()

    print("\n'" + p1_name + "' and '" + p2_name + "', you will play against each other.\n")
    return p1_name, p2_name

# Function to roll the dice
def get_dice_value():
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    dice_value = random.randint(1, DICE_FACE)
    print("Dice value: " + str(dice_value))
    return dice_value

# Function for snake bite
def got_snake_bite(old_value, current_value, player_name):
    print("\n" + random.choice(text_for_snake_bite).upper() + " ~~~~~~~~>")
    print("\n" + player_name + " got a snake bite. Going down from " + str(old_value) + " to " + str(current_value))

# Function for ladder jump
def got_ladder_jump(old_value, current_value, player_name):
    print("\n" + random.choice(text_for_ladder_jump).upper() + " ########")
    print("\n" + player_name + " is climbing the ladder from " + str(old_value) + " to " + str(current_value))

# Function for snake and ladder
def snake_ladder(player_name, current_value, dice_value):
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    old_value = current_value
    current_value = current_value + dice_value

    if current_value > MAX_VAL:
        print("You need " + str(MAX_VAL - old_value) + " to win this game. Keep trying.")
        return old_value

    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
    if current_value in snake_position:
        final_value = snake_position.get(current_value)
        got_snake_bite(current_value, final_value, player_name)

    elif current_value in ladders_position:
        final_value = ladders_position.get(current_value)
        got_ladder_jump(current_value, final_value, player_name)

    else:
        final_value = current_value

    return final_value

# Function to check the winner
def check_win(player_name, position):
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    if MAX_VAL == position:
        print("\n" + player_name + " has won the game!")
        print("Congratulations, " + player_name + "! You are the winner!")
        sys.exit(1)

# Function to play the game
def start():
    first_msg()
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    p1_name, p2_name = get_player_names()
    time.sleep(SLEEP_BETWEEN_ACTIONS)

    p1_current_position = 0
    p2_current_position = 0
    p1_snake_bites = 0
    p2_snake_bites = 0
    p1_ladder_climbs = 0
    p2_ladder_climbs = 0

    while True:
        # Player 1's turn
        input_1 = input("\n" + p1_name + ": " + random.choice(text_for_plr_turn) + " Press enter to roll the dice: ")
        print("\nDice is being rolled...")
        dice_value = get_dice_value()
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        print(p1_name + " is moving...")
        p1_current_position = snake_ladder(p1_name, p1_current_position, dice_value)
        check_win(p1_name, p1_current_position)

        # Player 2's turn
        input_2 = input("\n" + p2_name + ": " + random.choice(text_for_plr_turn) + " Press enter to roll the dice: ")
        print("\nDice is being rolled...")
        dice_value = get_dice_value()
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        print(p2_name + " is moving...")
        p2_current_position = snake_ladder(p2_name, p2_current_position, dice_value)
        check_win(p2_name, p2_current_position)

        # Count snake bites and ladder climbs for each player


        if p1_current_position in ladders_position.values():
            p1_ladder_climbs += 1
        if p2_current_position in ladders_position.values():
            p2_ladder_climbs += 1

        print("\n=== Game Results ===")
        print(p1_name + " had", p1_snake_bites, "snake bites and", p1_ladder_climbs, "ladder climbs.")
        print(p2_name + " had", p2_snake_bites, "snake bites and", p2_ladder_climbs, "ladder climbs.")

        # Determine the player with higher win probability
        if p1_snake_bites > p2_snake_bites:
            win_probability = p2_name
        elif p1_snake_bites < p2_snake_bites:
            win_probability = p1_name
        else:
            if(p2_current_position > p1_current_position):
                win_probability=p2_name
            elif(p1_current_position> p2_current_position) :
                win_probability=p1_name
            else :
                win_probability = "Both players have equal win probability"

        print("According to the count of snake bites and ladder climbs, the player with a higher win probability is:", win_probability)

start()
