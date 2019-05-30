from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

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

outside = Room(name="Outside Cave Entrance",
               message = "North of you, the cave mount beckons")
            #    exit_choices=['n'],
            #    room_id = 'outside')


foyer = Room(name="Foyer",
               message = """Dim light filters in from the south. 
               Dusty passages run north and east.""")
            #    exit_choices=['e', 'n', 's'],
            #    room_id = 'foyer')

overlook = Room(name="Grand Overlook",
               message = """A steep cliff appears before you, falling
                into the darkness. Ahead to the north, a light flickers in
                the distance, but there is no way across the chasm.""")
            #    exit_choices=['s'],
            #    room_id = 'overlook')

narrow = Room(name="Narrow Passage",
               message = """The narrow passage bends here from west
                to north. The smell of gold permeates the air.""")
            #    exit_choices=['n', 'w'],
            #    room_id = 'narrow')

treasure = Room(name="Treasure Chamber",
               message = """You've found the long-lost treasure
                chamber! Sadly, it has already been completely emptied by
                earlier adventurers. The only exit is to the south.""")
            #    exit_choices=['s'],
            #    room_id = 'treasure')

# Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(name=player1, current_room = 'outside')

print(player.name)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
