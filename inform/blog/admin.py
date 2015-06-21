from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    exclude = ['posted']
#    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)