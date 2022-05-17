from matplotlib.pyplot import cla


class Player:
    def __init__(self,pos_x,pos_y,character):
        self._pos_x=pos_x
        self._pos_y=pos_y
        self._character=character
    def GetPosX(self):
        return self._pos_x
    def GetPosY(self):
        return self._pos_y
    def GetCharacter(self):
        return self._character

class Goal(Player):
    def __init__(self, pos_x, pos_y, character):
        super().__init__(pos_x, pos_y, character)