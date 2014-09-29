Django Admin List Filter
======================


This plugin create combobox or list filter in django admin panel.

Quick start
-----------
1. First install Django Admin List Filter:

	```
	pip install git+git://github.com/witold-gren/djangoadmin-list-filters
	```
2. Usage class ComboboxFilter or SelectFilter in your list_filter:

	```
	from djangoadmin_list_filters.filters import ComboboxFilter, SelectFilter

	class ClassModelAdmin(admin.ModelAdmin):
		list_filter = [('field1', ComboboxFilter), ('field2', SelectFilter), 'field3']
	```