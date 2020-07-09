from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["head"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. All that remains is a single bent bronze coin. The only exit is to the south.""", ["coin"]),

    'cabin': Room("Your Cabin", """Your Cabin, sits in a pleasant clearing near a stream. It isn't much but it has the creature comforts""", ["bedroll"])

}


# Link rooms together

room['outside'].n_to = room['foyer']
room['outside'].s_to = room['cabin']
room['cabin'].n_to = room['outside']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])
# print(f'You are located at:\n{player.position.name}\n{player.position.description}')
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
while True:
    direction = input(
        "What do you feel like doing: N: North, E: East, S: South, W: West, C: Check Inventory, get + item name: pick up item, drop + item name: drop item, drop + it: drop most recent item, Q: Quit Game ")
    if len(direction.split(' ')) > 0:
        choice = direction.split(' ')
        verb = choice[0]
        if len(choice) == 2:
            obj = choice[1]
    if verb == 'q':
        break
    elif verb == "n":
        if player.position.n_to != None:
            player.position = player.position.n_to
            print(
                f'You are at: \n{player.position.name}\n{player.position.description}')
            player.position.items_in_room()
        else:
            print("There is nothing in that direction")
    elif verb == "s":
        if player.position.s_to != None:
            player.position = player.position.s_to
            print(
                f'You are at: \n{player.position.name}\n{player.position.description}')
            player.position.items_in_room()
        else:
            print("There is nothing in this direction")
    elif verb == "e":
        if player.position.e_to != None:
            player.position = player.position.e_to
            print(
                f'You are at: \n{player.position.name}\n{player.position.description}')
            player.position.items_in_room()
        else:
            print("There is nothing in this direction")
    elif verb == "w":
        if player.position.w_to != None:
            player.position = player.position.w_to
            print(
                f'You are at: \n{player.position.name}\n{player.position.description}')
            player.position.items_in_room()
        else:
            print("There is nothing in this direction")
    elif verb == "i":
        player.inventory()
    elif verb == 'get':
        if obj in player.position.items:
            player.pick_up(obj)
            player.position.items.remove(obj)
        else:
            print('There is no item in this room')
    elif verb == 'drop':
        if obj == "it":
            player.position.items.append(player.items[-1])
            player.discard(player.items[-1])
        else:
            player.discard(obj)
            player.position.items.append(obj)
    else:
        print("That is not a valid choice")
