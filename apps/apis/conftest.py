import pytest

from pytest_factoryboy import register

from apps.blog import factory as blog_factory

register(blog_factory.PostFactory)
register(blog_factory.CommentFactory)


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()
