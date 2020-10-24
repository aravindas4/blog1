import pytest

from django.urls import reverse

from apps.blog import models as blog_models


@pytest.mark.django_db
def test_post_list(api_client, post_factory):
    post_factory()
    post_factory()
    url = reverse('blog-post-list')
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.json()['results']) == blog_models.Post.objects.count()


@pytest.mark.django_db
def test_post_retrieve(api_client, post_factory):
    post1 = post_factory()
    url = reverse('blog-post-detail', kwargs={'pk': post1.uuid})
    response = api_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_create(api_client, post_factory):
    pass
