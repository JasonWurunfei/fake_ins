from django import template
from ..models import LikesAndDislikes

register = template.Library()

@register.simple_tag
def get_likes_number(content_type_id, object_id):
    try:
        count = LikesAndDislikes.objects.filter(content_type=content_type_id, object_id=object_id, like_type=True).count()
        return count
    except ContentType.DoesNotExist:
        return 'Unknown'

@register.simple_tag
def get_dislikes_number(content_type_id, object_id):
    try:
        count = LikesAndDislikes.objects.filter(content_type=content_type_id, object_id=object_id, like_type=False).count()
        return count
    except ContentType.DoesNotExist:
        return 'Unknown'