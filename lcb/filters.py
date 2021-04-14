from django_filters import rest_framework as filters


class BoardFilter(filters.FilterSet):

    owner = filters.CharFilter(method='filter_owner')
    member = filters.CharFilter(method='filter_member')

    def filter_owner(self, queryset, name, value):
        return queryset.filter(owner__username=value)

    def filter_member(self, queryset, name, value):
        return queryset.filter(members__username=value)
