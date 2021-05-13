from .Animal import Animal
from  Position import Position

class Antelope(Animal):
    def __init__(self, antelope=None, position=None, world=None):
        super(Antelope, self).__init__(antelope, position, world)

    def clone(self):
        return Antelope(self, None, None)

    def initParams(self):
        self.power = 2
        self.initiative = 6
        self.liveLength = 10
        self.powerToReproduce = 6
        self.sign = '&'


    def getNeighboringPositions(self):
        result = []
        positions = self.world.getNeighboringPositions(self.position)
        for pos in positions:
            Org = self.world.getOrganismFromPosition(pos)
            print(Org)
            if Org.__class__.__name__ == 'Wolf':
                antelope_next_pos_x = self.position.x + (self.position.x - Org.position.x)*2
                antelope_next_pos_y = self.position.y + (self.position.y - Org.position.y)*2
                if antelope_next_pos_x >= 0 and antelope_next_pos_x < self.world.worldX and antelope_next_pos_y >= 0 and antelope_next_pos_y < self.world.worldY:
                    result.append(Position(xPosition=antelope_next_pos_x,yPosition=antelope_next_pos_y))
                else:
                    print("Atakuję ")
                    antelope_next_pos_x = Org.position.x
                    antelope_next_pos_y = Org.position.y
                    result.append(Position(xPosition=antelope_next_pos_x, yPosition=antelope_next_pos_y))

                return result

        return self.world.filterPositionsWithoutAnimals(self.world.getNeighboringPositions(self.position))