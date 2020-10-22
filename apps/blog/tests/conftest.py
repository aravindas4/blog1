import operator
import pytest

from pytest_factoryboy import register

from apps.blog import factory as blog_factory

register(blog_factory.PostFactory)
register(blog_factory.CommentFactory)


def get_id(fixture_value):
    return fixture_value.get('id')


@pytest.fixture(params=[
        dict(operator=operator.eq, value=1, id='equal'),
        dict(operator=operator.le, value=2, id='less than'),
        dict(operator=operator.ge, value=0, id='greater than')
    ], ids=get_id)
def operators(request):
    return request.param
