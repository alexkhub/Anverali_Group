from django_filters import rest_framework as filters

from .models import *


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class VacancyFilter(filters.FilterSet):

    salary_min = filters.NumberFilter(field_name='salary_min', lookup_expr='gte')
    salary_max = filters.NumberFilter(field_name='salary_max', lookup_expr='lte')
    skills = CharFilterInFilter(field_name='skills__title', lookup_expr='in')
    date = filters.DateTimeFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Vacancy
        fields = ('salary_min', 'salary_max', 'skills', 'date')