from django import template

register = template.Library()

@register.filter
def splitter(name):
	new = name.split('-')
	return f'{new[0]} {new[1]}'
