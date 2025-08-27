from django.utils.text import slugify
import uuid

def create_slug(slug_id:str) ->str:
    from .models import blog
    slug_id = slugify(slug_id)
    while(blog.objects.filter(slug = slug_id).exists()):
        slug_id = f"{slugify(slug_id)}-{str(uuid.uuid4())[:4]}"

    return slug_id