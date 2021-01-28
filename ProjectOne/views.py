from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from scrapper.my_scrapper import scrap_contents

# Create your views here.

class MyCrawler(APIView):
        def post(self, request, *args, **kw):
            scrapper = scrap_contents(request.data['input'])
            response = Response(scrapper, status=status.HTTP_200_OK)
            return response
