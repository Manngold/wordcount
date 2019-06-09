from django.contrib import admin
from django.urls import path
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.home, name="home"),
    path('about/', myapp.views.about, name="about"),
    path('result/', myapp.views.result, name="result"),
]
