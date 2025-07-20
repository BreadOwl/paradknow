from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:pk>/', views.topic_edit, name='topic_edit'),
    path('delete/<int:pk>/', views.topic_delete, name='topic_delete'),
    path('topic/<int:pk>/', views.topic_detail, name='topic_detail'),
    path('question/edit/<int:pk>/', views.question_edit, name='question_edit'),
    path('question/delete/<int:pk>/', views.question_delete, name='question_delete'),
    path('topic/<int:topic_pk>/add-question/', views.question_add, name='question_add'),
    path('topic/<int:topic_pk>/checkyoslf/', views.checkyoslf, name='checkyoslf'),
]