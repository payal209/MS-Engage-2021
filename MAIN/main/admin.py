from django.contrib import admin
from .models import Category, Author, Comment, Post, Reply

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reply)
# Register your models here.
