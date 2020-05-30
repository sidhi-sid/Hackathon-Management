from django.contrib import admin
from django.urls import path, include
from .import views
# from products import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home1'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('login1/', views.login1, name='login1'),
    path('logout', views.logout, name='logout'),
    path('book', views.book, name='book'),

    path('homepage/', include('hackinfo.urls')),
    # path('blog/', include('blog.urls')),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
