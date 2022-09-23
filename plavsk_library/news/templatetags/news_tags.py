from django import template

register = template.Library()


@register.simple_tag()
def get_video_id(item):
    link = item['utub']
    return link.split('v=')[1]
