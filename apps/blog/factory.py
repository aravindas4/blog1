import factory

from faker import Factory as FakerFactory

from django.utils.text import slugify

from . import models as blog_models

fake = FakerFactory.create()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'auth.User'

    first_name = factory.Faker('name')
    email = factory.lazy_attribute(
        lambda obj: f"{slugify(obj.first_name)}@example.com")
    username = factory.lazy_attribute(lambda obj: f"{obj.email}")


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'blog.Post'

    title = fake.sentence()
    author = factory.SubFactory(UserFactory)
    body = fake.paragraph()
    publish = fake.date_time_this_decade(
        before_now=True, after_now=False, tzinfo=None).date()
    status = blog_models.Post.StatusChoice.PUBLISHED

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for tag in extracted:
                self.tags.add(tag)


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'blog.Comment'

    post = factory.SubFactory(PostFactory)
    name = fake.word()
    email = factory.lazy_attribute(
        lambda obj: f"{slugify(obj.name)}@example.com")
    body = fake.paragraph()
