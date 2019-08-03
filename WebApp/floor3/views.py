from django.shortcuts import render_to_response
# Create your views here.

def index(request):
	return render_to_response('floor3/templates/html/floor3.html')

