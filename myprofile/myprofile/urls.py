from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home ,name='home'),
    path('about/', views.about ,name='about'),
    path('service/', views.service ,name='service'),
    path('experience/', views.experience ,name='experience'),

    path('portfolio/', views.portfolio ,name='portfolio'),
    path('dtailprotflio/', views.dtailportfolio ,name='dtailprotflio'),

    path('price/', views.price ,name='price'),
    # path('team/', views.team ,name='team'),
    path('review/', views.review ,name='review'),
    path('contact/', views.contact ,name='contact'),

    path('blog/', views.blog ,name='blog'),
    path('dtail_post/', views.dtail_blog ,name='dtail_post'),

    



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




