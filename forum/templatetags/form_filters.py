from django import template
register = template.Library()

@register.filter(name='add_css_class_to_field')
def add_css_class_to_field(field, css):
   return field.as_widget(attrs={"class":css})