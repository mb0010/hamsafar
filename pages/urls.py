from django.urls import path
from django.contrib.auth import views as auth_views  
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path('add_trip/', views.add_trip, name='add_trip'),
    path('trip/<int:trip_id>/', views.view_trip_detail, name='view_trip_detail'),
    path('trip/<int:trip_id>/update/', views.update_trip, name='update_trip'),
    path('trip/<int:trip_id>/delete/', views.delete_trip, name='delete_trip'),
    path('add_companion_request/', views.add_companion_request, name='add_companion_request'),
    path('view_companion_requests/', views.view_companion_requests, name='view_companion_requests'),
    path('update_companion_request/<int:request_id>/', views.update_companion_request, name='update_companion_request'),
    path('delete_companion_request/<int:request_id>/', views.delete_companion_request, name='delete_companion_request'),
    path('companion-request/<int:id>/', views.view_companion_request_detail, name='view_companion_request_detail'),
    path('edit_companion_request/<int:id>/', views.edit_companion_request, name='edit_companion_request'),
    path('trip/<int:trip_id>/', views.view_trip_detail, name='view_trip_detail'),
]
