from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    # may want our home route to be named dashboard route. can change
    path('', views.user_list, name='user_list'),
    path('users/new', views.user_create, name='user_create'),
    path('users/<int:pk>', views.user_detail, name='user_detail'),
    path('users/<int:pk>/edit', views.user_edit, name='user_edit'),
    path('users/<int:pk>/delete', views.user_delete, name='user_delete'),

    path('goals/', views.goal_list, name='goal_list'),
    path('goals/new', views.goal_create, name='goal_create'),
    path('goals/<int:pk>', views.goal_detail, name='goal_detail'),
    path('goals/<int:pk>/edit', views.goal_edit, name='goal_edit'),
    path('goals/<int:pk>/delete', views.goal_delete, name='goal_delete'),
]