from apps.blog.models import Post, User
from apps.utils.serializers import BaseSerializer, BASE_FIELDS, ChoicesField


class UserSerializer(BaseSerializer):

    class Meta:
        model = User
        fields = '__all__'


class PostWriteSerializer(BaseSerializer):
    status = ChoicesField(choices=Post.StatusChoice)

    class Meta:
        model = Post
        exclude = BASE_FIELDS


class PostReadSerializer(PostWriteSerializer):
    author = UserSerializer()

    class Meta:
        model = Post
        exclude = BASE_FIELDS
