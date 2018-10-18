from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

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

def payload(board):
    payloads = {}
    board, index, score = minimax.main(board)
    payloads["data"] = board
    payloads["id"] = index
    payloads["status"] = score
    return payloads