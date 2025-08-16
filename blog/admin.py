from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-----'
    exclude = ['published_date']
    list_display = ['id','title','status','created_date','updated_date']
    list_filter = ['status']
    ordering = ['-created_date']
    search_fields = ['title','content']
    
admin.site.register(Post,PostAdmin)

# Register your models here.
