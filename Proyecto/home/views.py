from django.shortcuts import render

# Create your views here.



# def index(request):
# 	return render(request,"home/index.html"  ,{})
from .models import Tweet

def index(request):
	context = {
		"value": "Tweet xD",
		"object":Tweet.objects.get(id=3)
	 }

	return render(request, "tweet/index.html",context)


