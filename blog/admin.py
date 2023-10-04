from django.contrib import admin
from .models import Post,Description,Category,Comment
from django_summernote.admin import SummernoteModelAdmin

class DescriptionAdminInline(admin.StackedInline):
    model=Description
    fields=['subject','message']
    extra=0



@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    
    list_display=['title','updated_time','Active']
    date_hierarchy = "created_time"
    search_fields=('title','content')
    list_filter=('Active',)
    inlines=[DescriptionAdminInline]
    summernote_fields = ('content',)
    #fields=('title',)
    #exclude=['title']
    #list_display_links=['title','updated_time']
    #list_editable=('Active',)

class CommentAdmin(admin.ModelAdmin):
    list_dispaly=['name','created_time']
    search_fields=('subject','message')


# admin.site.register(Post,PostAdmin)
#admin.site.register(Description)
admin.site.register(Category)
admin.site.register(Comment,CommentAdmin)


