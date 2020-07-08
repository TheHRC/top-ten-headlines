from django.urls import path
from . import views
app_name = 'news'
urlpatterns =[
    path('home', views.news_list,name='home'),
    path('scrape/', views.scrape,name='scrape'),
    path('headlines/',views.news_headlines,name='headlines'),
]
