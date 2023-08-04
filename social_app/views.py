from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .models import *
from .serializers import *


class GetAllUsersApiView(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        data = CustomUserSerializer(users, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class GetUserPostsApiView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(CustomUser, pk=user_id)
        posts = Post.objects.filter(user=user)
        data = PostSerializer(posts, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class AddPostApiView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        new_post = PostAddSerializer(data=request.data, context={'user': request.user})
        if new_post.is_valid(raise_exception=True):
            new_post.save()
            return Response({'detail': 'Post is added!'}, status=status.HTTP_201_CREATED)


class DeletePostApiView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        if post.user == request.user:
            post.delete()
            return Response({'detail': 'Post is deleted!'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'This is not your post!'}, status=status.HTTP_403_FORBIDDEN)


