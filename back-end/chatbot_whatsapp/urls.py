from django.contrib import admin
from django.urls import path, include
# from .user_url import urlpatterns as user_urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include('faq.urls.user_url')),
    path("api/auth/", include('faq.urls.auth_url')),

]

