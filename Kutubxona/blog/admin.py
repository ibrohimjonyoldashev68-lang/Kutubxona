from django.contrib import admin
from .models import Author, Genre, Book, Member, Kirim, Chiqim

# Register your models here.
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Member)
admin.site.register(Kirim)
admin.site.register(Chiqim)