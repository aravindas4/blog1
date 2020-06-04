from rest_framework import routers

from . import api
router = routers.SimpleRouter()

router.register(r'', api.EmailModelViewSet, basename='emails-email')

urlpatterns = router.urls
