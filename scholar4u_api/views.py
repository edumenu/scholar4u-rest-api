from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters         # This is for the search feature

from . import serializers
from . import models


# Create your views here.
class PostsViewSet(viewsets.ReadOnlyModelViewSet):
    """Handles viewing posts"""
    serializer_class = serializers.PostSerializer
    queryset = models.Post.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('post_title', 'post_content','post_category')


class CommentsViewSet(viewsets.ReadOnlyModelViewSet):
    """Handles viewing posts"""
    serializer_class = serializers.CommentSerializer
    queryset = models.Comment.objects.all()
