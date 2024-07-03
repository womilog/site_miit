from django import template
from django.db.models import Count

from prepody.models import PrepodCategory


register = template.Library()


@register.inclusion_tag('prepody/list_categories.html')
def show_categories(cat_selected=0):
    cats = PrepodCategory.objects.annotate(total=Count('posts')).filter(total__gt=0)
    return {'cats': cats, 'cat_selected': cat_selected}