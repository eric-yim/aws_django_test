from django.urls import path

from . import views
app_name='projects'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<str:slug>/', views.DetailView.as_view(), name='detail'),
]
#urlpatterns = [
#    path('', views.index, name='index'),
#    path('<str:project_url_str>/', views.detail, name='detail'),
#]
