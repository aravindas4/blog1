from rest_framework import serializers
from taggit_serializer.serializers import (
    TagListSerializerField, TaggitSerializer)

from apps.blog import models as blog_models
from apps.utils.serializers import BaseSerializer, BASE_FIELDS, ChoicesField


class UserSerializer(BaseSerializer):

    class Meta:
        model = blog_models.User
        fields = '__all__'


class PostWriteSerializer(TaggitSerializer, BaseSerializer):
    status = ChoicesField(choices=blog_models.Post.StatusChoice)
    tags = TagListSerializerField()

    class Meta:
        model = blog_models.Post
        exclude = BASE_FIELDS


class CommentSerializer(BaseSerializer):
    class Meta:
        model = blog_models.Comment
        exclude = BASE_FIELDS


class PostReadSerializer(PostWriteSerializer):
    author = UserSerializer()
    comments = CommentSerializer(many=True)
    similar_posts = PostWriteSerializer(source='get_similar_posts', many=True)

    class Meta:
        model = blog_models.Post
        exclude = BASE_FIELDS
