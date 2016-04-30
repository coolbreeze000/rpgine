from django.shortcuts import render, render_to_response, redirect
from django.template import Context, RequestContext
from django.http import HttpResponse
import json

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def dashboard(request):
    return render_to_response('dashboard.html', context_instance=RequestContext(request))

@csrf_exempt
def roll(request):
    pass
    #data = json.loads(request.body)
    #response = HttpResponse(content_type='application/json-rpc')
    #return response.write('[0.81,0.15,0.87,0.24]')
    #return render_to_response('roll.html', context_instance=RequestContext(request))