"""This is a file defines the character class
"""
from objects import gameObject


class character(gameObject):
    def __init__(self, name, gender):
        super(character, self).__init__()
        self.name = name
        self.gender = gender
        self._status.update({'HP':100, 'AP':100, 'happyness': 100, 'strength': 0,
                       'endurance':0 , 'charisma':0, 'intelligence': 0,
                       'luck':0, 'stealth':0, 'consciousness':100})
        self.items = []
        self.location = None
        self.x_pos = 0.0
        self.y_pos = 0.0
        self.GPA = 0.0
        self.items_onhand = []
        self.skills = []
        self.money = 0
        self.age = 0

    def move(self, direction, units):
        pass

    def go_to(self, location):
        pass

    def pick_up(self, obj):
        pass

    def throw(self, obj, to_obj):
        pass

    def check(self, obj):
        pass

    def transfer_item(self, obj, to_obj):
        pass

    def use_item(self, obj, on_obj=None):
        for k, v in obj.effect.items():
            if on_obj is None:
                self._status[k] = self._status[k] + v
            else:
                on_obj._status[k] = on_obj._status[k] + v
    def learn_skills(self, obj):
        pass

    def make_obj(self, obj):
        pass

    def buy(self, obj, from_obj):
        cost = obj._status['value']
        if cost > self.money:
            print("Hey, go and make more money")
        else:
            self.money -= cost
            self.items += [obj,]

    def sell(self, obj, to):
        pass

    def trade(self, offer, request, target):
        pass

    def steal(self, obj, from_obj):
        pass
