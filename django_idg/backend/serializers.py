# tu_app/serializers.py
from rest_framework import serializers
from .models import Usuario
from django.contrib.auth.hashers import make_password

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = '__all__'

    def create(self, validated_data):
        pwd = validated_data.pop('password', None)
        if pwd is not None:
            validated_data['password'] = make_password(pwd)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        pwd = validated_data.pop('password', None)
        if pwd is not None:
            validated_data['password'] = make_password(pwd)
        return super().update(instance, validated_data)


