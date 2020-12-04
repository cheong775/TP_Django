from django.contrib import admin

# Register your models here.
#注册模型并把这些模型包含到管理后台里，让这些模型有管理的接口
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','status')
    list_filter = ('status','created','publish')
    search_fields = ('title','body')
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']



admin.site.register(Post,PostAdmin)
