from django.conf.urls import url
from django.urls import path
from .views import ActiveDriverView, ActiveDriverGetPassgersToSit, ActiveEditView, ActiveDriverGetPassgersToOut, ActiveDriverAllView

urlpatterns = [
    url('^active/sit/(?P<idstop>)$', ActiveDriverGetPassgersToSit.as_view()),
    path('active/create/', ActiveDriverView.as_view()),
    path('active/edit/<int:pk>/', ActiveEditView.as_view()),
    path('active/all/', ActiveDriverAllView.as_view()),
    url('^active/out/(?P<iddriver>)$', ActiveDriverGetPassgersToOut.as_view()),
]
