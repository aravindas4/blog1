from django.db import models
from django_fsm import FSMIntegerField
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from taggit.models import CommonGenericTaggedItemBase, TaggedItemBase

from apps.utils import utils
from apps.utils.models import BaseModel


class UUIDTaggedItem(CommonGenericTaggedItemBase, TaggedItemBase):
    object_id = models.CharField(
        max_length=10, verbose_name=_("object ID"), db_index=True)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class PostQueryset(models.QuerySet):

    def get_published(self):
        return self.filter(status=Post.StatusChoice.PUBLISHED)

    def get_similar_posts(self, post):
        return self.filter(
            tags__in=post.tags.values('id')).exclude(
            uuid=post.uuid).annotate(
            same_tags=models.Count('tags')).order_by('-publish')

    def get_search(self, value):
        return self.filter(
            models.Q(title__icontains=value) | models.Q(body__icontains=value)
        )


class Post(BaseModel):

    class StatusChoice(models.IntegerChoices):
        DRAFT = 0, _('Draft')
        PUBLISHED = 1, _('Published')

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(null=True, blank=True)
    status = FSMIntegerField(
        choices=StatusChoice.choices, default=StatusChoice.DRAFT)

    tags = TaggableManager(through=UUIDTaggedItem)

    objects = PostQueryset.as_manager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if not self.pk:
            self.slug = f'{slugify(self.title)}-{utils.get_uuid()}'

        if not self.publish and self.status in [self.StatusChoice.PUBLISHED]:
            self.publish = timezone.now()

        return super().save(*args, **kwargs)

    def get_similar_posts(self):
        return Post.objects.get_similar_posts(self)


class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
