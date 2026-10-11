"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}

# Set the player's starting room.
current_room = "Great Hall"

# Gameplay loop
while current_room != "exit":
    # 1. Display the current room.
    print(f"\nYou are in the {current_room}.")

    # 2. Prompt for a movement command or "exit".
    command = input("Enter direction (north, south, east, west) or 'exit': ").strip().lower()

    # 3. Branching decisions based on command
    if command == "exit":
        current_room = "exit"
    elif command in rooms[current_room]:
        # Valid direction for the current room
        current_room = rooms[current_room][command]
    else:
        # Invalid direction or unknown command
        print("Invalid move! Try again.")

print("Thanks for playing!")
