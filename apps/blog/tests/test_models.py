import pytest

from apps.blog import models as blog_models


@pytest.mark.django_db
def test_post_model(post_factory):
    post = post_factory()
    assert blog_models.Post.objects.count() == 1
    assert post.title == str(post)
