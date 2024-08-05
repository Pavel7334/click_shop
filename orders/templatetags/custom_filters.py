from django import template

register = template.Library()


@register.filter
def add_class(field, css_class):
    if not hasattr(field, 'as_widget'):
        return field  # Если это не поле формы, вернуть как есть

    return field.as_widget(attrs={'class': css_class})
