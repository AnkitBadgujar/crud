from django.contrib import admin
from django.urls import path
from .views import Home, AddStudent, DeleteStudent, EditStudent

urlpatterns = [
    path('',Home.as_view(),name='home' ),
    path('add_student',AddStudent.as_view(),name='add_student' ),
    path('delete_student',DeleteStudent.as_view(),name='delete_student' ),
    path('edit_student/<int:id>/',EditStudent.as_view(),name='edit_student' ),
]
