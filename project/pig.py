import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll


while True:
    player = input("enter the number of player(2-4): ")
    if player.isdigit():
        player = int(player)
        if 2 <= player <= 4:

            break
        else:
            print("must be btw 2 and 4")
    else:
        print("invalid try again")

max_score = 50
player_scores = [0 for _ in range(player)]

while max(player_scores) < max_score:

    for player_idx in range(player):
        print("\n player number", player_idx+1, "turn has just startd: ")
        current_score = 0
        while True:
            should_roll = input("would you like to roll(y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("you roll a 1! turn done.")
                current_score = 0
                break

            else:
                current_score += value
                print("you roll a : ", value)

            print("your score is :", current_score)

            player_scores[player_idx] += current_score

            print("your total score is : ", player_scores[player_idx])
