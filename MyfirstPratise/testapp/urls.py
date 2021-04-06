from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', views.admin_user, name='admin'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup_user, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('crud', views.crud, name='crud'),

    path('delete/<int:id>/', views.Delete, name='delete'),
    path('updates/<int:id>/', views.update_data, name='update'),
    path('', views.login, name='login'),
]