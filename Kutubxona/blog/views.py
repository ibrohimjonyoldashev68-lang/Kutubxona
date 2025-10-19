from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .models import Author, Genre, Book, Member, Kirim, Chiqim, Xabar
from .serializer import AuthorSerializer, GenreSerializer, BookSerializer, MemberSerializer, KirimSerializer, \
    ChiqimSerializer, XabarSerializer


class AuthorListAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GenreListAPIView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class MemberListAPIView(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class KirimListAPIView(generics.ListAPIView):
    queryset = Kirim.objects.all()
    serializer_class = KirimSerializer


class ChiqimListAPIView(generics.ListAPIView):
    queryset = Chiqim.objects.all()
    serializer_class = ChiqimSerializer


class XabarListCreateAPIView(generics.ListAPIView):
    queryset = Xabar.objects.all()
    serializer_class = XabarSerializer

