def start_game():
    # Welcome message
    print("Welcome to the Forest of Elara!")
    print("You are an adventurer on a quest to break the curse that has fallen upon the forest.")
    print("Your choices will determine the fate of Elara.")

    # Set the player's location
    player_location = "forest_entrance"

    # Game loop
    while True:
        # Check the player's location and display the corresponding description
        if player_location == "forest_entrance":
            print("You are standing at the entrance of the Forest of Elara.")
            print("To the north, you see a path leading deeper into the forest.")
            print("To the east, you see a faint glow coming from a clearing.")

            # Get the player's choice
            player_choice = input("What do you do? (north, east) ")

            # Update the player's location based on their choice
            if player_choice == "north":
                player_location = "forest_path"
            elif player_choice == "east":
                player_location = "clearing"
            else:
                print("Invalid choice. Please enter 'north' or 'east'.")

        elif player_location == "forest_path":
            print("You are following a winding path through the forest.")
            print("The trees are dense and the sunlight struggles to penetrate.")
            print("You hear strange noises coming from the shadows.")

            # Get the player's choice
            player_choice = input("What do you do? (continue, back) ")

            # Update the player's location based on their choice
            if player_choice == "continue":
                player_location = "abandoned_ruins"
            elif player_choice == "back":
                player_location = "forest_entrance"
            else:
                print("Invalid choice. Please enter 'continue' or 'back'.")

        elif player_location == "clearing":
            print("You emerge into a clearing bathed in an eerie glow.")
            print("In the center of the clearing, there is a shimmering portal.")
            print("You feel a strange pull towards the portal.")

            # Get the player's choice
            player_choice = input("What do you do? (approach, return) ")

            # Update the player's location based on their choice
            if player_choice == "approach":
                # This is a possible ending
                print("You step into the portal and are transported to a different world.")
                print("Congratulations! You have completed the game.")
                break
            elif player_choice == "return":
                player_location = "forest_entrance"
            else:
                print("Invalid choice. Please enter 'approach' or 'return'.")

        elif player_location == "abandoned_ruins":
            print("You stumble upon the ruins of an ancient city.")
            print("The buildings are crumbling and overgrown with vegetation.")
            print("You hear a faint voice calling out from the ruins.")

            # Get the player's choice
            player_choice = input("What do you do? (explore, leave) ")

            # Update the player's location based on their choice
            if player_choice == "explore":
                # This is a possible ending
                print("You explore the ruins and discover a hidden treasure.")
                print("Congratulations! You have completed the game.")
                break
            elif player_choice == "leave":
                player_location = "forest_path"
            else:
                print("Invalid choice. Please enter 'explore' or 'leave'.")

start_game()
