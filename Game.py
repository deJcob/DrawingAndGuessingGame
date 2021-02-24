
class Player:

    def __init__(self, name):
        self.nickName = name
        self.points = 0
        self.currentGameId = 0
        return

    def isDrawing(self):
        return False

    def CheckIsNameUnique(self):
        return True

class Game:
    def __init__(self):
        self.id = 1
        self.players = list[Player]



