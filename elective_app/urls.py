from django.urls import path
from elective_app import views
urlpatterns = [
    path('',views.renderIndex),
    path('renderUpdate/<int:id>',views.renderUpdatewithDetails),
    path('addStudent',views.addStudent),
    path('deleteStudent/<int:id>', views.deleteStudent),
    path('renderUpdate/updateStudent', views.updateStudent),

]