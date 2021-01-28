# URLconf
from django.urls import path

from .views import MyCrawler

urlpatterns = [
    path('my_scrapper/', MyCrawler.as_view()),
]