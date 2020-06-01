from django.urls import path, include
from hackinfo2 import views
# from products import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('register1/', views.register1, name='register1'),
    path('track/', views.track, name='track'),
    path('logout', views.logout, name='logout'),
    path('userdashboard', views.userdashboard, name='userdashboard'),
    path('organiserdashboard', views.organiserdashboard, name='organiserdashboard'),
    path('tracker', views.tracker, name='tracker'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
