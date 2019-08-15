from django.shortcuts import render_to_response
# Create your views here. A view is a Python function that takes a web request and returns a web response.

# Returns the display for the about page
def index(request):
	return render_to_response('about/templates/html/about.html')

