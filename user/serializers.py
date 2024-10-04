from rest_framework import serializers
from rest_framework.authtoken.models import Token

class CustomTokenSerializer(serializers.ModelSerializer):
    access_token = serializers.CharField(source='key', read_only=True)

    class Meta:
        model = Token
        fields = ('access_token',)
