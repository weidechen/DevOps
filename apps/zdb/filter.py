# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-6-7
# Author Yo
# Email YoLoveLife@outlook.com
import django_filters
from zdb import models

__all__ = [
   "ZDBInstanceFilter", "ZDBDatabaseFilter"
]


class ZDBInstanceFilter(django_filters.FilterSet):
    is_master = django_filters.CharFilter(method="is_master_filter")
    name = django_filters.CharFilter(method="name_filter")
    status = django_filters.CharFilter(method="status_filter")

    class Meta:
        model = models.DBInstance
        fields = ['is_master', 'name', 'status']

    @staticmethod
    def is_master_filter(queryset, first_name, value):
        return queryset.filter(is_master=value)

    @staticmethod
    def name_filter(queryset, first_name, value):
        return queryset.filter(name__icontains=value)

    @staticmethod
    def status_filter(queryset, first_name, value):
        return queryset.filter(_status=value)


class ZDBDatabaseFilter(django_filters.FilterSet):
    class Meta:
        model = models.DBDatabase
        fields = ['instance', ]