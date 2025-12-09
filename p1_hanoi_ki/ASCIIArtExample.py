# Example Class to show the specifications of the ASCII-Art-Output
# @Author Jan Strothmann


class ASCIIArtExample:
    def __init__(self):
        self.start_string="|  X||   ||   |\n| XX||   ||   |\n|XXX||   ||   |\n"
        self.play_string="|   ||   ||   |\n|   ||  X||   |\n|XXX|| XX||   |\n"
        self.end_string="|   ||   ||  X|\n|   ||   || XX|\n|   ||   ||XXX|\n"
        self.win_string="Winner!"
        self.error_string="Error"
        self.statenumber=0
        self.state=("Start","Play","End","Win")

    #Make the next move
    def move(self):
        self.statenumber+=1

    #Is the game still running
    def ended(self):
        ended=self.statenumber==3
        return ended

    def __str__(self):
        return_val=""
        #Since 3.10 Python has Switch-Case
        match self.state[self.statenumber]:
            case "Start":
                return_val=self.start_string
            case "Play":
                return_val=self.play_string
            case "End":
                return_val=self.end_string
            case "Win":
                return_val=self.win_string
            case _:
                return_val=self.error_string
        return "The Towers of Hanoi ("+self.state[self.statenumber]+"):\n"+return_val

game=ASCIIArtExample()
while not game.ended():
    print(game)
    game.move()
else:
    print(game)
