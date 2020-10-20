import pytest

from apps.blog import models as blog_models


@pytest.mark.django_db
def test_post_model(post_factory):
    post = post_factory()
    assert blog_models.Post.objects.count() == 1
    assert blog_models.Post.objects.count() <= 2
    assert blog_models.Post.objects.count() >= 0
    assert post.title == str(post)

    with pytest.raises(blog_models.Post.DoesNotExist,
                       match='Post matching query does not exist.'):
        blog_models.Post.objects.get(uuid=2345)

    # print('simple print')

    assert 0.1 + 0.2 == pytest.approx(0.3)
    assert [0.1 + 0.1, 0.2 + 0.1] == pytest.approx([0.2, 0.3])

    assert {"count": blog_models.Post.objects.count()} == pytest.approx(dict(count=blog_models.Post.objects.count()))


@pytest.mark.django_db
def test_comment_model(comment_factory):
    comment = comment_factory()
    queryset = blog_models.Comment.objects.all()
    assert queryset.count() == 1
    assert f'Comment by {comment.name} on {comment.post}' == str(comment)
