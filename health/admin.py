from django.contrib import admin
from .models import Post, Comment, Category, UpVote, DownVote
from django_summernote.admin import SummernoteModelAdmin



@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(UpVote)
class UpVoteAdmin(admin.ModelAdmin):
    list_display = ('post','user')


@admin.register(DownVote)
class DownVoteAdmin(admin.ModelAdmin):
    list_display = ('post','user')
