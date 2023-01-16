from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    # polls/create/
    path('create/', views.create_question, name='create_question'),
    # polls/
    path('', views.question_index, name='question_index'),
    # polls/1/
    path('<int:question_pk>/', views.question_detail, name='question_detail'),
    # polls/1/update/
    path('<int:question_pk>/update/', views.update_question, name='update_question'),
    # polls/1/delete/
    path('<int:question_pk>/delete/', views.delete_question, name='delete_question'),

    # polls/1/replies/create/
    path('<int:question_pk>/replies/create/', views.create_reply, name='create_reply'),
    # polls/1/replies/2/upvote/
    path('<int:question_pk>/replies/<int:reply_pk>/upvote/', views.reply_upvote, name='reply_upvote'),
    # polls/1/replies/2/delete/
    path('<int:question_pk>/replies/<int:delete_pk>/delete/', views.delete_reply, name='delete_reply'),
]