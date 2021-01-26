import six

from taggit_serializer.serializers import (
    TagListSerializerField, TaggitSerializer)

from apps.blog import models as blog_models
from apps.utils.serializers import BaseSerializer, BASE_FIELDS, ChoicesField


class UserSerializer(BaseSerializer):

    class Meta:
        model = blog_models.User
        fields = '__all__'


class CustomTagListSerializerField(TagListSerializerField):
    def to_internal_value(self, value):
        if isinstance(value, six.string_types):
            value = value.split(',')

        if not isinstance(value, list):
            self.fail('not_a_list', input_type=type(value).__name__)

        for s in value:
            if not isinstance(s, six.string_types):
                self.fail('not_a_str')

            self.child.run_validation(s)
        return value


class PostWriteSerializer(TaggitSerializer, BaseSerializer):
    status = ChoicesField(choices=blog_models.Post.StatusChoice)
    tags = CustomTagListSerializerField()

    class Meta:
        model = blog_models.Post
        exclude = BASE_FIELDS
        extra_kwargs = {
            "slug": {"required": False}
        }


class CommentSerializer(BaseSerializer):
    class Meta:
        model = blog_models.Comment
        exclude = BASE_FIELDS


class PostReadSerializer(PostWriteSerializer):
    author = UserSerializer()
    comments = CommentSerializer(many=True)
    # similar_posts = PostWriteSerializer(source='get_similar_posts', many=True)

    class Meta:
        model = blog_models.Post
        exclude = BASE_FIELDS
