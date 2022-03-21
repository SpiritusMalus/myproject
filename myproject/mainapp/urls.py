from myproject import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', main, name='main'),
    path('register/', Registration.as_view(), name='register'),
    path('', include('social_django.urls', namespace='social')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)