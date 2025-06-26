from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('catalog/', views.read, name='catalog'),
    path('catalog/create/', views.create, name='create_botanical'),
    path('catalog/delete/<int:id>/', views.delete, name='delete'),
    path('catalog/update/<int:id>/', views.update, name='update'),
    path('plantas/detais/<int:id>/', views.view, name='view'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
