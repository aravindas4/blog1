from django.apps import apps
from django.contrib import admin


class BaseModelAdmin(admin.ModelAdmin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_list = [i.name for i in self.model._meta.fields]
        self.list_display = field_list
        self.list_display_links = field_list

    def save_model(self, request, obj, form, change):

        if obj.pk:
            obj.modified_by = str(request.user.usrname)
        else:
            obj.created_by = str(request.user.username)

        super().save_model(request, obj, form, change)


my_app = apps.get_app_config('utils')

for model in list(my_app.get_models()):
    admin.site.register(model, BaseModelAdmin)
