from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:semester_id>/',views.CourseView,name='course'),
    path('<int:semester_id>/add/',views.addCourse,name='add')
]
