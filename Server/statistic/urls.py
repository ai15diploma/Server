from django.urls import path, include
from .views import StatisticCreateView, ScheduleAddView, ScheduleEditView , StatisticEditView

urlpatterns = [
    path('statistic/create/', StatisticCreateView.as_view()),
    path('statistic/<int:pk>/', StatisticEditView.as_view()),
    path('schedule/add/', ScheduleAddView.as_view()),
    path('schedule/edit/<int:pk>/', ScheduleEditView.as_view()),
]
