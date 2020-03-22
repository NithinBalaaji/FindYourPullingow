from django.urls import path
from .views import (
   CreateGroup,
   SingleGroup,
   ListGroups,
   JoinGroup,
   LeaveGroup

)
from . import views
from django.urls import reverse_lazy



urlpatterns = [
    path('',ListGroups.as_view(), name='groups-list'),
    path('new/',CreateGroup.as_view(), name = 'groups-create'),
    path('<int:pk>/',SingleGroup.as_view(), name = 'single-group'),
    path('join/<int:pk>/', JoinGroup.as_view(), name='group-join'),
    path('leave/<int:pk>/', LeaveGroup.as_view(), name='group-leave'),

]


