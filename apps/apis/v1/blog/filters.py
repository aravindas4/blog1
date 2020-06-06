from django_filters import rest_framework as dj_filters
from apps.blog.models import Post


class PostFilter(dj_filters.FilterSet):
    year = dj_filters.NumberFilter(field_name='publish__year')
    month = dj_filters.NumberFilter(field_name='publish__month')
    search = dj_filters.CharFilter(action='searches')

    class Meta:
        model = Post
        fields = ['year', 'month']

    def searches(self, queryset, value, *args, **kwargs):
        return queryset.get_search(value)
