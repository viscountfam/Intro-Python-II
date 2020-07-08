# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = items

    def __str__(self):
        return f"{self.name}, {self.description}"
    
    def picked_from_room(self, item):
        self.items.remove(item)

    def dropped_in_room(self, item):
        self.items.append(item)

    def items_in_room(self):
        if self.items:
            if len(self.items):
                print("****************\n Items in this room:")
                for x in self.items: 
                    print(x) 
        else:
            print("there is no item here")               