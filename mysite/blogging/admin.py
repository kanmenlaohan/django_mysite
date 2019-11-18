from django.contrib import admin
from blogging.models import Post, Category


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 2


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
     (None, {'fields': ['title']}),
     ('Post Content', {'fields': ['text']}),
    ]
    inlines = [CategoryInline]


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
