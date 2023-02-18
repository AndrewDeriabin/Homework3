import random


class Human:
    def __init__(self, name="Human"):
        self.name = name
        self.revolver = Revolver()
        self.alive = True

    def game_death(self):
        if self.revolver.revolver == True:
            print("I'm dead")
        else:
            print("I'm alive")


class Revolver:
    def __init__(self):
        self.revolver = list(revolver_list.values())[random.randint(0, 1)]['bullet']


revolver_list = {'Rev1': {'bullet': True},
                 'Rev2': {'bullet': False}}

john = Human(name='John')
john.game_death()
