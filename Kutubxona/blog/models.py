from django.db import models

# Create your models here.
class Author(models.Model):
    nomi = models.CharField(max_length=100)
    tugilgan_yili = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.nomi


class Genre(models.Model):
    nomi = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nomi


class Book(models.Model):
    nomi = models.CharField(max_length=200)
    muallif = models.ForeignKey(Author, on_delete=models.CASCADE)
    janr = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    yili = models.CharField(max_length=4, blank=True, null=True)
    miqdori = models.IntegerField(default=0)
    mavjud = models.IntegerField(default=0)
    img = models.ImageField(upload_to="img/book", blank=True, null=True)

    def __str__(self):
        return self.nomi


class Member(models.Model):
    fio = models.CharField(max_length=150)
    email = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.fio


class Kirim(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    miqdori = models.IntegerField(default=1)
    qachondir = models.DateTimeField(auto_now_add=True)
    narxi = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.book.nomi} (keldi)"


class Chiqim(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    miqdori = models.IntegerField(default=1)
    qachondir = models.DateTimeField(auto_now_add=True)
    qaytarilganmi = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.book.nomi} → {self.member.fio}"



class Xabar(models.Model):
    ism = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    matn = models.TextField(blank=True, null=True)
    yuborilgan_vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ism}: {self.matn[:20]}"