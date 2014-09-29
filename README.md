Django Admin List Filter
--

<pre>
from djangoadmin_list_filters.filters import ComboboxFilter, SelectFilter

class ClassModelAdmin(admin.ModelAdmin):
	list_filter = [('field1', ComboboxFilter), ('field2', SelectFilter), 'field3']
</pre>

This plugin create combobox or list filter in django admin panel.