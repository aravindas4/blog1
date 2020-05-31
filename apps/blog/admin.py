from django.apps import apps
from django.contrib import admin

from apps.utils.admin import BaseModelAdmin

my_app = apps.get_app_config('blog')

for model in list(my_app.get_models()):
    admin.site.register(model, BaseModelAdmin)
