from rest_framework.routers import DefaultRouter
from django.urls import path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from .views import (
    AuthorListAPIView,
    GenreListAPIView,
    BookListAPIView,
    MemberListAPIView,
    KirimListAPIView,
    ChiqimListAPIView, XabarListCreateAPIView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Kutubxona",
        default_version='v1',
        description="Bu API hujjatlari Swagger va Redoc orqali ko'rsatiladi",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns =[
    path('authors/', AuthorListAPIView.as_view(), name='authors'),
    path('genres/', GenreListAPIView.as_view(), name='genres'),
    path('books', BookListAPIView.as_view(), name ='books'),
    path('members', MemberListAPIView.as_view(), name ='members'),
    path('kirim/', KirimListAPIView.as_view(), name='kirim'),
    path('chiqim/', ChiqimListAPIView.as_view(), name='chiqim'),
    path('Xabar/', XabarListCreateAPIView.as_view(), name='xabar'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]





