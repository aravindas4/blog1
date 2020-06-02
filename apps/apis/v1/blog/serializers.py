from apps.blog.models import Post
from apps.utils.serializers import CWNModelSerializer, BASE_FIELDS, ChoicesField


class PostWriteSerializer(CWNModelSerializer):
    status = ChoicesField(choices=Post.StatusChoice)

    class Meta:
        model = Post
        exclude = BASE_FIELDS


class PostReadSerializer(PostWriteSerializer):

    class Meta:
        model = Post
        exclude = BASE_FIELDS
