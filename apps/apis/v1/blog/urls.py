from rest_framework import routers

from . import api

router = routers.SimpleRouter()

router.register(r'post', api.PostModelViewSet, basename='blog-post')
router.register(r'comment', api.CommentModelViewSet, basename='blog-comment')

urlpatterns = router.urls
