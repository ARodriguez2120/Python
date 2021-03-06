"""tweet_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from home import views

app_name = "tweets"

urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    path('list_tweets/', views.list_tweets.as_view(), name="list_tweets"),
    path('detail_tweet/<int:pk>', views.DetailTweet.as_view(), name="detail_tweet"),
    path('create/', views.create.as_view(), name="create_tweet"),
    path('update/<int:pk>', views.updateTweet.as_view(), name="update_tweet"),
    path('delete/<int:pk>', views.deleteTweet.as_view(), name="delete_tweet"),

]
    