from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),  # Trailing slash added
    path('signup/', views.signup, name='signup'),  # Trailing slash added
    path('signin/', views.signin, name='signin'),  # Trailing slash added
    path('signout/', views.signout, name='signout'),  # Trailing slash added
    path('dashboard/', views.dashboard, name='dashboard'),  # Trailing slash added
    path('upload/', views.upload_image, name='upload_image'),  # Already correct
]
