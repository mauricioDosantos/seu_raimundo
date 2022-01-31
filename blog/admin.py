from django.contrib import admin
from .models import Post, Attachment, Tag, Visualized, Contacts, AreaLabel


admin.site.register(Post)
admin.site.register(Attachment)
admin.site.register(Tag)
admin.site.register(Visualized)
admin.site.register(Contacts)
admin.site.register(AreaLabel)
