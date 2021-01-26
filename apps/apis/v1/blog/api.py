from django_filters import rest_framework as dj_filters
from rest_framework.viewsets import ModelViewSet

from . import filters as blog_filters
from . import serializers as blog_serializers
from .serializers import blog_models


class PostModelViewSet(ModelViewSet):
    serializer_class = blog_serializers.PostWriteSerializer
    queryset = blog_models.Post.objects.all()
    filter_backends = [dj_filters.DjangoFilterBackend, ]
    filter_class = blog_filters.PostFilter

    def get_queryset(self):
        self.queryset = self.queryset.select_related(
            'author'
        ).prefetch_related(
            'comments', 'tags', 'author__groups', 'author__user_permissions'
        )

        if self.action in ['list', 'retrieve']:
            return self.queryset.get_published()

        return self.queryset.all()

    def get_serializer_class(self):

        if self.action in ['list', 'retrieve']:
            return blog_serializers.PostReadSerializer

        return self.serializer_class


class CommentModelViewSet(ModelViewSet):
    serializer_class = blog_serializers.CommentSerializer
    queryset = blog_models.Comment.objects.all()
