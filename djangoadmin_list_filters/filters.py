# -*- coding: utf-8 -*-
from django.contrib import admin


__author__ = 'witoldgren'


class SelectFilter(admin.AllValuesFieldListFilter):
    """
    Utworzenie filtru z znacznika select.

    example:

    class RatingVisitAdmin(admin.ModelAdmin):
        list_filter = ('author', ('external_user', SelectFilter))
    """
    template = 'admin/filter_select.html'


class ComboboxFilter(admin.AllValuesFieldListFilter):
    """
    Utworzenie filtru z combobox.

    example:

    class RatingVisitAdmin(admin.ModelAdmin):
        list_filter = ('active', ('external_user', ComboboxFilter))
    """
    template = 'admin/filter_combobox.html'