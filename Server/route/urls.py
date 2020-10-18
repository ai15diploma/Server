from django.contrib import admin
from django.urls import path, include
from route.views import StopListView, RouteListView, RouteDetailView, EditRoute, EditStop, StopDetailView

urlpatterns = [
    path('stop/all', StopListView.as_view()),
    path('route/all', RouteListView.as_view()),
    path('route/<int:pk>', RouteDetailView.as_view()),
    path('stop/<int:pk>', StopDetailView.as_view()),
    path('edit_stop/<int:pk>', EditStop.as_view()),
    path('edit_route/<int:pk>', EditRoute.as_view()),
]
