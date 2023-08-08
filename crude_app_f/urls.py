from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard_home/', views.dashboard_home, name = 'dashboard_home'),
    path('BannerAdd/', views.BannerAdd, name = 'BannerAdd'),
    path('BannerView/<pk>', views.BannerView, name = 'BannerView'),
    path('BannerEdit/<title>', views.BannerEdit, name = 'BannerEdit'),
    path('BannerDelete/<pk>', views.BannerDelete, name = 'BannerDelete'),
    path('ArticleAdd/', views.ArticleAdd, name = 'ArticleAdd'),
    path('ArticleView/<pk>', views.ArticleView, name = 'ArticleView'),
    path('ArticleEdit/<title>', views.ArticleEdit, name = 'ArticleEdit'),
    path('ArticleDelete/<pk>', views.ArticleDelete, name = 'Articledelete'),
]
