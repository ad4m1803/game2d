class Board:
    def __init__(self):
        self._board=[  
                [" "," "," "," "],
                [" "," "," "," "],
                [" "," ","x"," "],
                [" "," "," "," "]]
    def Reset(self):
        pass
    def Display(self):
        for x in self._board:
            for y in x:
                print("[",end="")
                print(y,end="")
                print("]",end="")
            print()
    def SetPosition(self,chr,x,y):
        pass