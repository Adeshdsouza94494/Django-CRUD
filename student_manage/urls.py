
from django.urls import path
from student_manage import views


urlpatterns = [
    path('', views.list_student, name='home'),
    path("update/<int:id>",views.update_student,name="update"),
     path("delete/<int:id>",views.deletedata,name="delete"),
     path("add/",views.add_student,name="add"),
      path('search_student/', views.searchstudent, name='searchstudent'),
]
