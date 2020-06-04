from apps.blog.models import Post, User
from apps.utils.serializers import CWNModelSerializer, BASE_FIELDS, ChoicesField


class UserSerializer(CWNModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class PostWriteSerializer(CWNModelSerializer):
    status = ChoicesField(choices=Post.StatusChoice)

    class Meta:
        model = Post
        exclude = BASE_FIELDS


class PostReadSerializer(PostWriteSerializer):
    user = UserSerializer()

    class Meta:
        model = Post
        exclude = BASE_FIELDS
