import pytest

from apps.blog import models as blog_models

timeout = pytest.mark.timeout(1, method='thread')


@pytest.mark.django_db
def test_post_model(operators, post_factory):
    post = post_factory(tags=['xyx'])
    opera = operators.get('operator')
    value = operators.get('value')
    assert opera(blog_models.Post.objects.count(), value)
    assert post.title == str(post)

    with pytest.raises(blog_models.Post.DoesNotExist,
                       match='Post matching query does not exist.'):
        blog_models.Post.objects.get(uuid=2345)

    assert 0.1 + 0.2 == pytest.approx(0.3)
    assert [0.1 + 0.1, 0.2 + 0.1] == pytest.approx([0.2, 0.3])

    assert {"count": blog_models.Post.objects.count()} == pytest.approx(dict(count=blog_models.Post.objects.count()))

    post2 = post_factory(tags=['xyx'])
    assert post.get_similar_posts().exists() is True


# @pytest.mark.xfail(strict=False)
@pytest.mark.django_db
def test_comment_model(comment_factory):
    comment = comment_factory()
    queryset = blog_models.Comment.objects.all()
    assert queryset.count() == 1
    assert f'Comment by {comment.name} on {comment.post}' == str(comment)
