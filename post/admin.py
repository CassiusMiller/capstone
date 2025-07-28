from django.contrib import admin
from .models import Post, Status, Location, Type
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'created_on', 'Location', 'Status', 'Type'
    ]

admin.site.register(Post, PostAdmin)
admin.site.register(Status)
admin.site.register(Location)
admin.site.register(Type)