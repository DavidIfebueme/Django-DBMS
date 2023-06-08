from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.user_form),
    path('list/',views.user_list)
]
