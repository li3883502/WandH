from django import template
# 这里与教程不同
from ..models import Article, Category, Bigcategory, Carousel
from django.db.models.aggregates import Count
from django.utils.html import mark_safe
import re


register = template.Library()


@register.simple_tag
def get_bigcategory_list():
    return Bigcategory.objects.all()


@register.simple_tag
def get_category_list(id):
    return Category.objects.filter(bigcategory_id=id)


@register.simple_tag
def get_carousel_index():
    return Carousel.objects.filter(number__lte=5)

