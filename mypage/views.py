from django.http import HttpResponse
from django.shortcuts import render
from mypage.logic.content import dashBoardContent

content = dashBoardContent()

def home(request):
    try:
        return render(request, "index.html", {})
    except Exception as e:
        text = """<h1>Error !</h1>"""+ str(e)
        return HttpResponse(text)

def dashboard(request):
    return render(request, "dashboard.html", {"content":content})



