from djoser.serializers import TokenCreateSerializer
from djoser.serializers import TokenSerializer

class CustomTokenCreateSerializer(TokenCreateSerializer):
    pass

class CustomTokenSerializer(TokenSerializer):
    pass
post todos
{
  "title": "string",
  "description": "string",
  "completed": true,
  "user": 2
}
{
  "title": "string",
  "description": "string",
  "completed": true,
  "user": 2
}