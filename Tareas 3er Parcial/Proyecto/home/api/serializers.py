from rest_framework import serializers

from home.models import Tweet



class TweetModelSerializer(serializers.ModelSerializer):
	

	class Meta:
		model = Tweet
		fields = [
			"content",
			"timerstarp",
		]

