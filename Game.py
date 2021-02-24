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
    minGuessingTime = 60
    maxGuessingTime = 120
    timeStep = 10
    gameId = None
    waitingTime = None
    Players = []
    timer = 0

    def __init__(self, waiting_time, game_id, creator_name):
        self.gameId = game_id
        self.Players.append(Player(creator_name))


