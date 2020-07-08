from django.urls import path
from . import views

app_name = "finance"

urlpatterns =[
    path('', views.company_article_list, name='companies'),
    path('api/chart/data/', views.CharData.as_view(), name='api-char-data'),
]
