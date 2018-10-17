from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . IAMorpion import julesIA as IA
from . IAMorpion import minimax

import json

# Create your views here.

def index(request):
    return render(request,'index.html')

@csrf_exempt
def sendData(request):
    if request.method == 'POST':
        # read request body
        data = json.loads(request.body)
        # read payload
        data = payload(data)
        # convert dict format to json
        data = json.dumps(data)
        return HttpResponse(data)

# def payload(grille):
#     payloads = {}
#     grille2 = IA.f(grille)
#     if IA.end(grille2) != 0:
#         return(grille, IA.end(grille2), -1)
#     else:
#         grille2, choix = IA.IA_fini(grille2)
#     payloads["data"] = IA.f_1(grille, choix)
#     payloads["id"] = choix
#     payloads["status"] = IA.end(grille2)
#     print(choix)
#     return(payloads)

def payload(board):
    payloads = {}
    board, index, score = minimax.main(board)
    print(board, index, score)
    payloads["data"] = board
    payloads["id"] = index
    payloads["status"] = score
    return(payloads)