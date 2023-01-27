from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.throttling import UserRateThrottle
from rest_framework.exceptions import Throttled

# Create your views here.
#create a django rest framework POST view to add information to the Client Model

from rest_framework import generics
from .models import Client
from .serializers import ClientSerializer

class CreateClientView(generics.CreateAPIView):
    """Create a new client in the system"""
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    throttle_classes = [UserRateThrottle]

    def throttled(self, request, wait):
        raise Throttled(detail={
              "message": f"Transaction limit exceeded, try again in {round(wait)} seconds"
        })

    def post(self, request, *args, **kwargs):
        """Handle POST requests to create a new client"""

        # Get the data from the request body and save it as a new client
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data.get("name")
        self.perform_create(serializer)

        return Response({'message': f'Client {name} created successfully!'}, status=status.HTTP_201_CREATED)

    