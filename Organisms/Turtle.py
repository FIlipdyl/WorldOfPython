from .Animal import Animal
from random import  randint,choice
from Action import Action
from ActionEnum import ActionEnum
from Position import Position


class Turtle(Animal):
    def __init__(self, turtle=None, position=None, world=None):
        super(Turtle, self).__init__(turtle, position, world)

    def clone(self):
        return Turtle(self, None, None)

    def initParams(self):
        self.power = 1
        self.initiative = 1
        self.liveLength = 30
        self.powerToReproduce = 15
        self.sign = '#'
        self.round_in_stomach = 0

    def consequences(self, atackingOrganism):
        result = []
        if self.power > atackingOrganism.power:
            result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, atackingOrganism))
        else:
            self.round_in_stomach = 2
            self.in_animal = atackingOrganism.position
            result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, self))
        return result


    def move(self):
        result = []
        if self.round_in_stomach == 0:
            pomPositions = self.getNeighboringPositions()
            newPosition = None
            if pomPositions:
                newPosition = choice(pomPositions)
                result.append(Action(ActionEnum.A_MOVE, newPosition, 0, self))
                self.lastPosition = self.position
                metOrganism = self.world.getOrganismFromPosition(newPosition)
                if metOrganism is not None:
                    result.extend(metOrganism.consequences(self))
        else:
            self.round_in_stomach -= 1
            if self.round_in_stomach == 0:
                newPosition = choice(self.world.filterPositionsWithoutAnimals(self.world.getNeighboringPositions(self.in_animal)))
                result.append(Action(ActionEnum.A_OUT, newPosition, 5, self))
        return result

    def getNeighboringPositions(self):
        return self.world.filterPositionsWithoutAnimals(self.world.getNeighboringPositions(self.position))