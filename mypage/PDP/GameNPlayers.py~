class GameNPlayers:

    #The structure of the stages -> numStage: [state, ganacia, entropia, valorSeleccionado], ...
    #The structure of the probabilities -> state: probability of this state 

    def __init__ (self, probabilities = {}, states = [] ):
        self.probabilities = probabilities
        self.states = states
	self.stages = 0
        
    ##This method create the tables of probabilistic dynamic programing 
    def createTables(self):
        numStages = len(self.stages)
        for stage in range(numStages, 1, -1):
            ##For each stage it is necesary to calc the entropy of the next stage
            entropia = self.calcEntropy(stage)
            table = []
            for state in self.states:
                row = []
                row.append(state) ##Pos 0
                ganancia = self.getGanancia(state, stage)
                row.append(ganancia) ## Pos 1 
                row.append(entropia) ## Pos 2
                mayor = max(ganancia, entropia)
                row.append(mayor) ##  Pos 3 This is the value that is choose as the option
                if mayor is ganancia  and entropia is ganancia :
                    row.append("End/Continue") ## Pos 4
                elif mayor is ganancia :
                    row.append("End") ## Pos 4
                else:
                    row.append("Continue") ## Pos 4
                table.append(row)
            self.stages[stage] =  table
 
    ##This method calc the entropy so the probability of exit in the next stage
	##This method uses the Theorem of Total Probability 
    def calcEntropy(self, currentStage):
        entropy =0
        if currentStage < len(self.stages) :
            #print len(self.stages)
            #print currentStage
            previousStage = self.stages[currentStage+1] #This give me the  previous stage
            for rows in previousStage:
                entropy += rows[3]*self.probabilities[rows[0]]                    
        return entropy


	##This method gives me the gain of  each state in each stage
    def getGanancia(self, state, stage):
        #print(stage)
        if state.isdigit():
            state2 = int(state)
            funcion = 'state2*2'
        else:
            if(state is "injured"):
                return -10
            if(state is "unscathed"):
                return 0
            if(state is "almost"):
                return 10
        return eval(funcion)


    def getStages(self):
        return self.stages

    def setStages(self, stages):
        self.stages = stages

    def setProbabilities(self,probabilities):
		self.probabilities = probabilities

    def setStates(self, states):
		self.states = states
