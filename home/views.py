from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User

from home.serializers import LoginSerializer, RegisterSerializer

from rest_framework.views import APIView
from rest_framework import viewsets, status

from django.contrib.auth import authenticate
    

    
class RegisterAPI(APIView):

    # def get(self, request):
    #     users = User.objects.all()
    #     serializer = RegisterSerializer(users, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data = data)

        if not serializer.is_valid():
            return Response({
                'status': False,
                'message': serializer.errors
                } ,status.HTTP_400_BAD_REQUEST)
        serializer.save()

        return Response({'status': True, 'message': 'User created'}, status.HTTP_200_OK)
    

# APIView - It allows you to define the HTTP methods (e.g. GET, POST, PUT, DELETE) that the view should handle
class LoginAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data = data)
        if not serializer.is_valid():
            return Response({
                'status': False,
                'message': serializer.error
            }, status.HTTP_400_BAD_REQUEST)
        print(serializer.data)
        
        user = authenticate(username = serializer.data['username'], password = serializer.data['password'])

        if not user:
            return Response({
                'status': False,
                'message': 'Invalid Credentials'
            }, status.HTTP_400_BAD_REQUEST)
        
        return Response({'status': True, 'message': 'user_logIn'}, status.HTTP_201_CREATED)