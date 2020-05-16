from django.urls import path

from . import views

app_name = 'My_Blogs'

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('<int:blog_id>/', views.detail, name='detail')
]
