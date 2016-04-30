from django.shortcuts import render, render_to_response, redirect
from django.template import Context, RequestContext

# Create your views here.

def dashboard(request):
    return render_to_response('dashboard.html', context_instance=RequestContext(request))