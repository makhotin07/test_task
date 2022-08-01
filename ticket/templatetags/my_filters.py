from django import template

register = template.Library()


@register.filter(name = 'add_class')
def add_class(value, arg):
	return value.as_widget(attrs = {'class': arg})


@register.filter(name = 'add_attr')
def add_attr(value, attribute_input):
	count = attribute_input.count('///')
	attrs_dict = {}
	if count == 1:
		attr_name, attr_value = attribute_input.split('///')
		attrs_dict = {attr_name.strip(): attr_value.strip()}
	elif count > 1:
		list_attrs = attribute_input.split('|')
		for attrs in list_attrs:
			attr_name, attr_value = attrs.split('///')
			attrs_dict[attr_name.strip()] = attr_value.strip()
	else:
		pass
	return value.as_widget(attrs = attrs_dict)


@register.filter(name = "make_small_textarea")
def normalize_textarea(value):
	return value.as_widget(attrs = {
		'rows': 2,
		'cols': 40,
		'style': 'height: 15px;'
	})


