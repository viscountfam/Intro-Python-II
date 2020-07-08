# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, position):
        self.position = position
        self.items = []
    
    def inventory(self):
        if len(self.items):
            print('Your inventory is empty')
        else:
            print("These item(s) are in your inventory")
            for item in self.items:
                print(item)
    def pick_up(self, item):
        self.items.append(item)
        print(f'You have picked up a {item}')
    
    def discard(self, item):
        self.items.remove(item)
    