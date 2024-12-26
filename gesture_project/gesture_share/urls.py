from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('image/<int:pk>/', views.image_detail, name='image_detail'),
    path('get-user-ip/', views.get_user_ip, name='get_user_ip'),
    path('receiver/', views.receiver_view, name='receiver'),
    path('check-image/', views.check_image, name='check_image'),
    path('capture_image/', views.capture_image, name='capture_image'),
    path('camera/', views.camera_view, name='camera_view'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)