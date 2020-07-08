from django.urls import path
from . import views

app_name = 'notepad'

urlpatterns = [
    path('create/', views.create_view, name='create'),
    path('list/', views.list_view, name='list'),
    path('<int:id>/delete/', views.delete_view, name='delete'),
    path('<int:id>/update/', views.update_view, name='update'),

]
