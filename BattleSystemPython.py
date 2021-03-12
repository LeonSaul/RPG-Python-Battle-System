# Mini Battle System Game
# Made By: Saul Leon
# --------------------- Updates-------------------------------------
# Restructer code cleanup for the battle system.

enemy_hp: int = 6
player_hp: int = 5
win_score: int = 0

def Battle_intro():
    print("What will you do?\n")
    print("1.) Fight\n")
    print("2.) Escape in fear\n")
    print("Please type either 1 for Fight or 2 for Escape.\n")

def Battle_Commands():
    print("What will you do?\n")
    print("For Attack type Attack\n")
    print("For Defend type Defend\n")
    print("For a Special move type Special\n")
    #END

def End_trigger():
    print("No valid inputs have been made:")
    print("The game has ended please restart.")

    #end
print("(Okay this is scary but I can do this! You say to yourself.)\n")
print("There is a thunderstorm going on only you and the evil boss standing in the middle of a ruined battle field.\n"
      "The final battle with you and him is about to begin, how this all ends is up to you. Can you defeat baddy bad?\n")


print("Fighting yay! A monster appears from the marsh its up to you to stop it.\n")

Battle_intro()

#command = int(input())
option = int(input(">"))
#----------------------------------------------------------------------------------------------------------------------------
if option == 1:
    print("'----------------Battle: Player Phase----------.'\n")
    Battle_Commands()
    command = input()

    while enemy_hp <= 6:
        if command in ['Attack', 'attack']:
            print("\n")
            print("You bash the monsters head with the closest thing you can find\n")
            print("Monster staggers, its a hit!\n")
            enemy_hp = enemy_hp - 1 #Everytime they attack 1HP get's taken out of the enemy.
            print('Monster HP:', enemy_hp)
            print("\n")

#----------------------------------------------------------------
        if enemy_hp <= 3:
            print("The monster claws at you!\n")
            print("You took three damage!\n")
            player_hp = player_hp -1
            print('Player HP:', player_hp)
     #-----------------------------------------------------------
            if not enemy_hp != 0: #When the enemy's HP reaches zero battle ends and story continues.
                print("Congrats you survived the battle!\n")
                win_score = win_score + 1
                break
        #-----------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------------------
        #The second command the player can use, protects them from attacks.
        elif command in ['Defend', 'defend']:
            print("You protected yourself from the enemy! You got no damage.\n")
            command = input('What will you do now?\n')
            #Battle_Commands()
    #-----------------------------------------------------------------------------------------------------------------------------
        elif command in ['Special', 'special']:
            print("You decide to use a special move but it might take awhile.\n")
            command = input('Battle: What will you do now?\n')
            #Battle_Commands()
    #-----------------------------------------------------------------------------------------------------------------------------

        else:
            End_trigger()
            break

#-----------------------------------------------------------------------------------------------------------------
if option == 2:
    print("You decide to run away...\n")
    print("\n")
    print("Its not very effective\n")
    print("The team laughs at you for being a coward.")
    #End
#--------------------------------------------------------------------------------------------------------------------

if win_score == 1:
    print("'----------------Story: Phase----------.'\n")
    print("The monster is gone but that's not the end of the war here. A man approches ready for another fight!\n")
    Battle_Commands()

