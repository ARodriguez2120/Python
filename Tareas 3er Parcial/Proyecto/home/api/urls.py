
from django.urls import path
from home.api import views


app_name = "api_tweets"

urlpatterns = [
	path('api/list_tweet/', views.ListTweetAPIView.as_view(), name="ListAPIView")



]