from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LocSerializer
from .models import Location

from rest_framework.permissions import IsAuthenticated
import requests
import json

# Create your views here.

class LocView(viewsets.ModelViewSet):
    serializer_class = LocSerializer
    queryset = Location.objects.all()

class GenerateLoc(APIView):
    """ This view make and external api call, save the result and return 
        the data generated as json object """
    # Only authenticated user can make request on this view
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        response = {}
        # Make an external api request ( use auth if authentication is required for the external API)
        r = requests.get('http://api.positionstack.com/v1/forward?access_key=2b96d1c0475bd1a00c5a36c52b8209ef&query=' + request)
        r_status = r.status_code
        # If it is a success
        if r_status == 200:
            # convert the json result to python object
            data = json.loads(r.text)
            # Loop through the credentials and save them
            # But it is good to avoid that each user request create new
            # credentials on top of the existing one
            # ( you can retrieve and delete the old one and save the news credentials )
            for c in data:
                credential = Location(name=c, address=c, city=c, state=c)
                credential.save()
            response['status'] = 200
            response['message'] = 'success'
            response['information'] = data
        else:
            response['status'] = r.status_code
            response['message'] = 'error'
            response['information'] = {}
        return Response(response)


class UserLoc(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request, format=None):
        current_user = self.request.user
        credentials = Location.objects.filter(user__id=current_user)
        return Response(credentials)
