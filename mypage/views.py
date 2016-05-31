from django.http import HttpResponse
from django.shortcuts import render
from mypage.logic.content import dashBoardContent
from PDP.Game2Player import  Game2Player  
from PDP.GameNPlayers import  GameNPlayers
from PDP.Player import  Player
from PDP.testLogic import  testProgram

content = dashBoardContent()

def home(request):
    try:
        return render(request, "index.html", {})
    except Exception as e:
        text = """<h1>Error !</h1>"""+ str(e)
        return HttpResponse(text)

def dashboard(request):

    return render(request, "dashboard.html", {"content":content})

def dynamicProgramming(request):
    nStates = request.POST.get("nStates", False)
    numStages = int(request.POST.get("nStages", False)) 
    apuesta = int(request.POST.get("bet", False))

    if(nStates != False):
        n = int(nStates)
        probabilities = {}
        for i in range (1,n+1):
            val = float(request.POST.get(str(i), False))
            probabilities[str(i)] = val
        print probabilities
        print nStates
        print numStages
        print apuesta

        
        states=probabilities.keys()
        game = GameNPlayers(probabilities,states)
        data = testProgram(game, numStages, probabilities, apuesta)

    return render(request, "dynamicProgramming.html", {"data":data})

def boltzman(request):
    return render(request, "boltzman.html", {})
