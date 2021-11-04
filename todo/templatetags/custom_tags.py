from django import template

register = template.Library()

def splitter(name):
	new = name.split('-')
	return f'{new[0]} {new[1]}'
