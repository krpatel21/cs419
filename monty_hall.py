import random

GOAT = 0
CAR = 1

def get_door():
    a = random.randint(0, 1)
    b = 0
    c = 0

    if (a != 1):
        b = random.randint(0, 1)

    if (a != 1 and b != 1):
        c = 1

    door = [a, b, c]
    return door


print get_door()


def choose_other_door(choice, doors):
    ran = 0
    while (ran != choice and doors[choice] != CAR):
        ran = random.randint(0, 2)
    return ran


def choose_random_door(choice):
    ran = 0
    while (ran != choice):
        ran = random.randint(0, 2)
    return ran


def play_game():
    choice = random.randint(0, 2)
    door = [0, 1, 2]
    doors = get_door()

    if (doors[choice] == CAR):
        host_choice = choose_random_door(choice)
    else:
        host_choice = choose_other_door(choice, doors)

    for i in door:
        if (i != choice and i != host_choice):
            swap = i
    if (doors[swap] == CAR):
        return "win"
    else:
        return "loss"


def score():
    wins = 0
    i = 0
    while (i < 100):
        result = play_game()
        if (result == "win"):
            wins= wins+1
        i = i + 1

    return float(wins)/i

print score()
print score()
print score()
print score()
print score()
print score()
print score()
print score()
print score()
print score()
