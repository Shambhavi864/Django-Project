from rest_framework import serializers
from .models import Person

from django.contrib.auth.models import User


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

    def validate(self, data):
        special_characters = "\.[]{}()<>*+-=!?^$|;@{}[],/%#:"
        if any(c in special_characters for c in data['name']):
            raise serializers.ValidationError('name should not contain any speacial characters')
        if data['age']<18:
            raise serializers.ValidationError('age should be greater than 18')
        return data

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):

        if data['username']:
            if User.objects.filter(username = data['username']).exists():
                raise serializers.ValidationError('username is taken')
            
        if data['email']:
            if User.objects.filter(username = data['email']).exists():
                raise serializers.ValidationError('email already exists')
        return data
    
    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'], email = validated_data['email'], password = validated_data['password'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data
        print(validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()