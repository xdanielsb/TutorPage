from __future__ import print_function

class Player:

    
    name = ""
    factor = ""    
    ##Features of the players
    features = {
        "speed" : 0.0,
        "strength" : 0.0,
        "intelligent" : 0.0,
        "shield" : 0.0,
        "skill" : 0.0,
        "espirit" : 0.0,
        "confidence" : 0.0,
		"health": 0.0
    }
    def show(self):
		for feature in self.features:
			print (feature + " " + str(self.features[feature]))

    def __init__(self,name, features):
        self.features = features
        self.calcFactor()

    def getFeatures(self):
        return self.features

    def setFeatures(self):
        self.features = features
	
    def calcFactor(self):
		features = self.features
		self.factor= features["health"] * 0.15 \
					+ features["confidence"]*0.15 \
					+ features["speed"]*0.1 \
					+ features["strength"]*0.1 \
					+ features["intelligent"]*0.19 \
					+ features["shield"]*0.01 \
					+ features["skill"]*0.1 \
					+ features["espirit"]*0.2 

    def getFactor(self):
		return self.factor
    
