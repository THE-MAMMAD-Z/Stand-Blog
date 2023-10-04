from django import template
from ..models import Post,Category

register=template.Library()

@register.simple_tag
def hello(name):
    return f'hello world {name}'


@register.filter
def upper(value):
    return value.upper()

@register.inclusion_tag('blog/blog-recent.html')
def recent_posts():
    posts=Post.objects.filter(Active=1).order_by('-updated_time')
    return {'posts':posts}

@register.inclusion_tag('blog/blog-categories.html')
def categories():
    category=Category.objects.all()
    posts=Post.objects.filter(Active=1)
    
    Dict={}
    
    for cat in category:
        Dict[cat]=posts.filter(category=cat).count()
        
    return {'Dict':Dict}
    
    


