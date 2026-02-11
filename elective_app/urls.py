from django.urls import path
from elective_app import views
urlpatterns = [
    path('',views.renderIndex),
    path('api/getInformation',views.GetInfo)
]