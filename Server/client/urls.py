from django.contrib import admin
from django.urls import path, include
from .views import ClientCreateView, ClientEditView , ClientListView

urlpatterns = [
    path('active/create/', ClientCreateView.as_view()),
    path('active/edit/<int:pk>', ClientEditView.as_view()),
    path('active/all/', ClientListView.as_view()),
]
