from rest_framework.serializers import ModelSerializer
from .models import *


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostAddSerializer(ModelSerializer):
    class Meta:
        model = Post
        exclude = ['user',]

    def create(self, validated_data):
        validated_data["user"] = self.context["user"]
        return super().create(validated_data)
