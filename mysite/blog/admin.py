from blog.models import Post
from django.contrib import admin

class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Date information', {'fields': ['pub_date'],'classes':['collapse']}),
        (None,               {'fields': ['post']})
    ]
    list_display = ('title','post','was_published_today')
    list_filter = ['pub_date']
    search_fields = ['post']
admin.site.register(Post,BlogAdmin)
