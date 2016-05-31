from GameNPlayers import GameNPlayers

class Game2Player(GameNPlayers):

    #The structure of the stages -> numStage: [state, ganacia, entropia, valorSeleccionado], ...
    #The structure of the probabilities -> state: probability of this state 

	##Posible states : wounded, unscathed
	###injured : when the factor of  the player 1 is much less than the second player
	###unscathed : when the factor  of  the player 1 is biggest than the second player
	###almost : when the factor of the player 1 is almost equal of the second player
	

    ##This method is the constructor
    def __init__ (self,  probabilities = {}, states = [] ):
        self.probabilities = probabilities
        self.states = states
        self.factor = 0

    def calcProbabilities(self, player1, player2):
        self.factor = player1.getFactor()-player2.getFactor()
        probabilities = self.probabilities		
        if(self.factor<=-20):
			probabilities["injured"] = 0.6
			probabilities["unscathed"] = 0.1
			probabilities["almost"]= 0.3
        elif(self.factor>-20 and self.factor<=20):
			probabilities["injured"] = 0.2
			probabilities["unscathed"] = 0.7
			probabilities["almost"]= 0.1
        else:
			probabilities["injured"] = 0.1
			probabilities["unscathed"] = 0.4
			probabilities["almost"]= 0.5	
        return probabilities		
