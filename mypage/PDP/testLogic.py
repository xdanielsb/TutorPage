## This file contents the test for the logic in the script probabilistic dynamic programing
## author: Daniel Fernando Santos Bustos


from __future__ import print_function
from Game2Player import  Game2Player  
from GameNPlayers import  GameNPlayers
from Player import  Player


def testProgram(game, numStages, probabilities ,apuesta):
    
    stages = {} ##This var store the tables in the game 
    content = ''
    ##Here I initialize the stages 
    for x in range (1, numStages+1):
        stages[x] = []

    ##Instantiate the class Game1Player
    game.setStages(stages)
    game.createTables()
    stages = game.getStages()

    ##This is the first decision that the program recomend to take
    ##calEntropy(1) refers to calc the probabiliti to win more money if won in the next stage
    cadena = ''
    cadena = 'Amount of money that you can win in the first stage '+str(game.calcEntropy(1))+ '<br><br>Stage# 1 <br>'
    content += 'Entropy to win the next stage'+str(game.calcEntropy(1))+ '<br><br>Stage#1<br>'
    print ('Entropy win next stage'+str(game.calcEntropy(1))+ '\n\nStage#1')
    if apuesta>game.calcEntropy(1):
        print ('We recomend do not play, but if you want to play we suggest that you follow this instructions \n')
        content += 'We recomend do not play, but if you want to play we suggest that you follow this instructions <br><br>'
    else:
        print ('We recomend that you play, We suggest that you follow this instructions \n')
        content += 'We recomend that you play, We suggest that you follow this instructions <br><br>'

    ##These are the next stages (2 to num of stages) in the game
    ##Here we show the piece of advices that our game give
    content += "Please push the button for looking the recomenadtions " 
    for i in range (2, numStages+1):
        
        print ('Stage #'+str(i)) 
        content += "<button type='button' class='btn btn-default' data-toggle='modal' data-target='#"+str(i)+"'>"
        content += "  Stage 	&nbsp;"+str(i)
        content += "</button>&nbsp;"
        
        table= stages[i]
        aux = "<ul>"
        aux = "<li>RECOMENDATIONS</li>"
        for row in table:
            aux += '<li>If your state is '+ row[0]+ ', We recomend that you '+ row[4] +' the game'+"</li>"
            #print (aux)
	    aux += "</ul>"
        content += "<div class='modal fade' id='"+str(i)+"' tabindex='-1' role='dialog' aria-labelledby='myModalLabel'>"
        content += "  <div class='modal-dialog' role='document'>"
        content += "    <div class='modal-content'>"
        content += "      <div class='modal-header'>"
        content += "        <button type='button' class='close' data-dismiss='modal' aria-label='Close'><span aria-hidden='true'>&times;</span></button>"
        content += "        <h4 class='modal-title' id='myModalLabel'> Data Stage "+str(i)+"</h4>"
        content += "      </div>"
        content += "      <div class='modal-body'>"
        content += "        "+aux
        content += "      </div>"
        content += "      <div class='modal-footer'>"
        content += "        <button type='button' class='btn btn-default' data-dismiss='modal'>Close</button>"
        content += "      </div>"
        content += "    </div>"
        content += "  </div>"
        content += "</div>"      


    return content	

def test1Player():
    numStages = 10 ##This is the number of stages
    probabilities = {} ##This dictionary store the probabilities in the game
    apuesta = 0 ##This is the initial bet of the game

    ##Define  the probabilities of this case
    probabilities['1'] = 0.3
    probabilities['2'] = 0.25
    probabilities['3'] = 0.2
    probabilities['4'] = 0.15
    probabilities['5'] = 0.1
	#			state    probability of this state  	

    states=probabilities.keys()
    game = GameNPlayers(probabilities,states)
    testProgram(game, numStages, probabilities, apuesta)


