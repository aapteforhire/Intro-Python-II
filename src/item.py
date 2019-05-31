# Write a class to hold item information for players

class Item():

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return self.name

    def on_take(self):
        return f"You have picked up {self.name} which is {self.description}"

    # def on_drop(self):
    #     return f"You have dropped off {self.name}"

