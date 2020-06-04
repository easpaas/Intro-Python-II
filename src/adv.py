from room import Room
from player import Player

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
## Main
#

print("Welcome adventurer! \n")

# Create a new player and intialize to outside 
newPlayer = Player(room['outside'])

#
## tries to move the player in the specified direction 
#
def try_direction(player, direction):
    attribute = direction + '_to'

    if hasattr(player.location, attribute):
        # use getattr to fetch the value associated with the attribute 
        # update our player's location with the fetched room 
        player.location = getattr(player.location, attribute)
    else:
        print("There's nothing in that direction!")

#
## Game loop
# 
while True:
    print("\n")
    print(newPlayer.location)

    # * Waits for user input and decides what to do.
    first_char = input("\nfirst_char: ").strip().lower().split()
    first_first_char = first_char[0]
    first_char = first_first_char[0]

    # If the user enters "q", quit the game.
    if first_char == 'q':
        break

    # If the user enters a cardinal direction, attempt to move to the room there.
    # strip off everything but the first char 
    if first_char == 'n':
        # move to the north
        try_direction(newPlayer, first_char)
    elif first_char == 's':
        # move to the south
        try_direction(newPlayer, first_char)
    elif first_char == 'e':
        # move to the east 
        try_direction(newPlayer, first_char)
    elif first_char == 'w':
        # move to the west 
        try_direction(newPlayer, first_char)