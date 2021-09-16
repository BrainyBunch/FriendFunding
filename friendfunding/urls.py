from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('goal/', views.goal_list, name='goal_list'),
    path('user/new', views.user_create, name='user_create'),
    path('goal/new', views.goal_create, name='goal_create'),
    path('user/<int:pk>', views.user_detail, name='user_detail'),
    path('goal/<int:pk>', views.goal_detail, name='goal_detail'),
    path('goal/<int:pk>/edit', views.goal_edit, name='goal_edit'),
    path('user/<int:pk>/edit', views.user_edit, name='user_edit'),
    path('goal/<int:pk>/delete', views.goal_delete, name='goal_delete'),
    path('user/<int:pk>/delete', views.user_delete, name='user_delete'),
    path('random/', views.random, name='random')
    # path('users/', views.UserList.as_view(), name='user_list'),
    # path('user/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    # path('goal/', views.GoalList.as_view(), name='goal_list'),
    # path('goal/<int:pk>', views.GoalDetail.as_view(), name='goal_detail')
]