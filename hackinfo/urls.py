from django.urls import path, include
from .import views
# from products import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('track/', views.track, name='track'),
    path('logout', views.logout, name='logout'),
    # path('book', views.book, name='book'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
