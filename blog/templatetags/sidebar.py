from django import template
from blog.models import *

register = template.Library()


@register.inclusion_tag('blog/menu_popular_posts_tpl.html')
def get_popular(cnt=3):
    posts = Blog.objects.order_by('-views')[:cnt]
    return {"posts": posts}


@register.inclusion_tag('blog/tags_tpl.html')
def get_tags():
    tags = Tag.objects.all()
    return {"tags": tags}


@register.inclusion_tag('blog/category_tpl.html')
def get_category():
    category = Category.objects.all()
    return {'categories': category}
