from django.urls import include, path

from .blog import urls as blog_urls
from .emails import urls as emails_urls

urlpatterns = [
    path('blog/', include(blog_urls)),
    path('emails/', include(emails_urls)),
]
