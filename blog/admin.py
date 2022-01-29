from django.contrib import admin
from .models import Post, Attachment, Tag, Visualized


admin.site.register(Post)
admin.site.register(Attachment)
admin.site.register(Tag)
admin.site.register(Visualized)
