from django.shortcuts import render

# Create your views here.
from .models import Tweet
from .forms import FormCreate
from django.views import generic

def index(request):
	context = {
		"message": "Este es un mensaje desde la vista index",
		"numerico": 6574,
		"array": [1,2,3,4],
		"dic": {"a":12, "b": 23},
	 }

	return render(request, "tweet/index.html",context)

# CRUD #

def list_tweets(request):
	queryset = Tweet.objects.all()
	context= {
		"tweets": queryset

	}
		
	return render(request, "tweet/list_tweets.html",context)


def detail_tweet(request, id=1):
	queryset = Tweet.objects.get(id=id)
	context={
		"tweet_object": queryset
	}
	return render(request, "tweet/details.html", context)


def create(request):
	form = FormCreate(request.POST or None) 
	if request.POST:
		if form.is_valid():
			form.save()
	else:
		form = FormCreate(request.POST or None)

	context = {
		"form":form
	}
	return render(request, "tweet/create.html", context)

class list_tweets (generic.ListView):
	template_name="tweet/list_tweets.html"
	model=Tweet



class updateTweet (generic.UpdateView):
	template_name="tweet/update.html"
	model=Tweet
	fields=["content"]
	success_url="/list_tweets/"


class deleteTweet (generic.DeleteView):
	template_name="tweet/delete.html"
	model=Tweet
	success_url="/list_tweets/"


class create (generic.CreateView):
	template_name="tweet/create.html"
	model=Tweet
	fields=["content"]
	success_url="/list_tweets/"

class DetailTweet (generic.DetailView):
	template_name="tweet/details.html"
	model=Tweet

