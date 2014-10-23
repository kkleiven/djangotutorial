from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': ":D"}
    return render_to_response('cmu_prints/index.html', context_dict, context)
def index2(request):
    return HttpResponse("Made by Kim Kleiven, Kirn Hans, Jenna Choo, Clark Chen.")
