from django import template

register = template.Library()

@register.filter
def first_three_words(text):
    words = text.split()
    return ' '.join(words[:3])
