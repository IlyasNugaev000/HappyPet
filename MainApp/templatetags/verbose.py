from django import template
register = template.Library()


@register.filter
def get_verbose_field_name(obj, field_name):
    return obj._meta.get_field(field_name).verbose_name.title()