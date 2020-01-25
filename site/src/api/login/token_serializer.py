from rest_framework import serializers


# TODO Check if all 3rd party sign in has token size at most 2048 bytes
class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=2048)
