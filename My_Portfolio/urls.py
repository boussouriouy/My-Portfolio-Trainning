from django.urls import path

from . import views
app_name = 'My_Portfolio'
urlpatterns = [
    path('home/', views.home, name='home')
]
