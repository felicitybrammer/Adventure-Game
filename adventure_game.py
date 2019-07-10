import time
import random

monsters = random.choice(['pirate', 'giant', 'witch', 'goblin', 'dragon'])


def print_sleep(string, seconds):
    print(string)
    time.sleep(seconds)


# print the intro
def intro():
    print_sleep("You find yourself standing in a nearly empty parking lot.", 2)
    print_sleep("Rumor has it that a " + monsters + " is somewhere around here"
                " and has been terrorizing the local shopping mall.", 3)
    print_sleep("To the left of you is a big, green dumpster.", 2)
    print_sleep("To your right is a sinister-looking van with darkened "
                "windows.", 2)
    print_sleep("In your hand you hold your trusty (but not very effective) "
                " pepper spray.", 2)


# check for valid input
def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_sleep("That is not an option. Please try again.", 2)
    return response


# approach the van and make another choice
def van(items):
    print_sleep("You approach the van.", 2)
    print_sleep("You are about to knock when the door slides open and out "
                "steps a " + monsters + ".", 2)
    print_sleep("This is the " + monsters + "'s lair!", 2)
    print_sleep("The " + monsters + " attacks you!", 2)
    fight_run_choice(items)


# approach the dumpster to find the sword
def dumpster(items):
    if 'sword' not in items:
        print_sleep("You peer cautiously into the dumpster.", 2)
        print_sleep("There's quite a lot of stinky garbage in there.", 2)
        print_sleep("But wait! You spot a shiny object and pull it out.", 2)
        print_sleep("You have found the poisonous " + monsters + " sword!", 2)
        print_sleep("You get rid of your useless pepper spray.", 2)
        items.append('sword')
    elif 'sword' in items:
        print_sleep("There's nothing new to find here.", 2)
    print_sleep("You head back to the parking lot.", 2)
    make_choice(items)


# choose the van or the dumpster
def make_choice(items):
    print_sleep("Enter 1 to try to open the doors of the van.", 2)
    print_sleep("Enter 2 to look inside the dumpster.", 2)
    response = valid_input("What would you like to do? \n"
                           "(Please enter 1 or 2.)", '1', '2')
    if response == '1':
        van(items)
    elif response == '2':
        dumpster(items)


# choose to fight or run away from the pirate in the van
def fight_run_choice(items):
    fight_run = valid_input("Would you like to (1) fight or (2) run "
                            "away?" "Please enter 1 or 2.", '1', '2')
    if fight_run == '1':
        # fight with the pepper spray
        if 'sword' not in items and 'already_used' not in items:
            print_sleep("You hold up your measly can of pepper spray with a "
                        "shaky hand.", 2)
            print_sleep("You spray until there's nothing left.", 2)
            print_sleep("The " + monsters + " smirks and starts to laugh!", 2)
            print_sleep("The " + monsters + " attacks you again!", 2)
            items.append('already_used')
            fight_run_choice(items)
        # fight with the sword
        elif 'sword' in items:
            print_sleep("You pull out the shiny poisonous " + monsters +
                        " sword.", 2)
            print_sleep("You slay the " + monsters +
                        " in one quick motion.", 2)
            print_sleep("You saved the shopping mall!", 2)
            play_again()
        # fight with no weapons
        elif 'already_used' in items:
            print_sleep("You pull out your pepper spray but it's empty!", 2)
            print_sleep("The " + monsters + " lunges and kills you.", 2)
            print_sleep("GAME OVER.", 2)
            play_again()
    elif fight_run == '2':
        # run away
        print_sleep("You run back into the parking lot. Luckily, you don't "
                    "seem to have been followed.", 2)
        make_choice(items)


def play_again():
    choice = valid_input("Would you like to play again?"
                         "Please say 'yes' or 'no'?", 'yes', 'no')
    if 'no' in choice:
        print_sleep("Goodbye.", 2)
    elif 'yes' in choice:
        print_sleep("OK", 2)
        play_game()


def play_game():
    items = []
    intro()
    make_choice(items)
    play_again()


play_game()
