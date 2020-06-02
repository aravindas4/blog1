from django.urls import include, path

from .blog import urls as blog_urls

urlpatterns = [
    path('blog/', include(blog_urls))
]
