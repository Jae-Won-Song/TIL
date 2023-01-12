from django.urls import path  
from . import views


app_name = 'board'

urlpatterns = [
    # articles/create/
    path('create/', views.create_article, name='create_article'),
    path('', views.article_index, name='article.index'),    
    path('<int:article_pk>/', views.article_detail, name='article_detail'),
    path('<int:article_pk>/comments/create/', views.create_comment, name='create_comment'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),
]
