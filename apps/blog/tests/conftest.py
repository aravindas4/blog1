from pytest_factoryboy import register

from apps.blog import factory as blog_factory

register(blog_factory.PostFactory)
register(blog_factory.CommentFactory)
