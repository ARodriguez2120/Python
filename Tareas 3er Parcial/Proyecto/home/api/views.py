from rest_framework import generics
from home.api. serializers import TweetModelSerializer
from home.models import Tweet





class ListTweetAPIView(generics.ListAPIView):
	serializer_class = TweetModelSerializer

	def get_queryset(self, *args, **kwargs):
		return Tweet.objects.all()