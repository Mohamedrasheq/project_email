from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.web1,name="page_2"),
    path('enter/',views.index,name="home")
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)