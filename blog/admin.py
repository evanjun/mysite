from django.contrib import admin
from .models import BlogArticles
# Register your models here.
#admin.site.register(BlogArticles)

class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publish")
    list_filter = ("publish", "author")
    search_fields = ("title", "body")
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ['publish', 'author']

admin.site.register(BlogArticles, BlogArticlesAdmin)

# class BlogArticlesAdmin(admin.ModelAdmin):
#     list_display = ("title", "author", "publish") #admin后台显示的字段
#     list_filter = ("publish", "author") #匹配过滤字段
#     search_fields = ("title", "body") #搜索字段
#     raw_id_fields = ("author",)
#     date_hierarchy = "publish"
#     ordering = ["publish", "author"]# 排序
