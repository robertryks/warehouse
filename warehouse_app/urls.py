from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('grades/', views.grade_list, name='grade_list'),
    path('grades/add', views.grade_add, name='grades_add'),
]
