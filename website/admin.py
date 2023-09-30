from django.contrib import admin
from .models import Category, Post, SiteProfile

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    
    # causes issues with styling
    # fieldsets = (
    #     (None, {'fields':
    #         (('title',
    #         'slug',
    #         'status',
    #         'is_about',
    #         'author'),
    #          ), 
    #         'description':'General Post Information'}),
    #     ('Content', {'fields':
    #         ('header_image',
    #          'content',
    #          ),
    #         'description':'The object has to have these attributes'}),
    #     ('SEO', {'fields':
    #         ('categories',
    #          'seo_teaser'
    #          ),
    #         'description':'The object has to have these attributes'}),
    #     )
    # jazzmin_section_order = (None, "Content", "Seo")

admin.site.register(Post, PostAdmin)
admin.site.register(SiteProfile)
admin.site.register(Category)