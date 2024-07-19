from rest_framework.decorators import api_view
from rest_framework.response import Response

from home.models import Person
from home.serializers import PeopleSerializer, LoginSerializer, RegisterSerializer

from rest_framework.views import APIView
from rest_framework import viewsets, status

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

    

#All the apis that a person can hold --> GET, POST, PUT, DELETE
#api view class
class PersonAPI(APIView):
    def get(self, request):
        objs = Person.objects.all()
        serializer = PeopleSerializer(objs, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def patch(self, request):
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(obj, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
        
    def delete(self, request):
        data = request.data
        obj = Person.objects.filter(id = data['id'])
        obj.delete
        return Response({'message': 'person deleted'})
    

    
class RegisterAPI(APIView):

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


        token, _ = Token.objects.get_or_create(user = user)
        return Response({'status': True, 'message': 'user_logIn', 'token': str(token)}, status.HTTP_201_CREATED)


    
class PeopleViewSet(viewsets.ModelViewSet):
    serializer_class = PeopleSerializer
    query = Person.objects.all()