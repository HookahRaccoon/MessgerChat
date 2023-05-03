from django.urls import path
from django.contrib import admin
from.import views
from .views import ProfileDetailView, ProfileUpdateView

urlpatterns = [
    path("", views.index, name="index"),
    path('<str:room_name>/', views.room, name='name'),
    path('user/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('user/<str:slug>/', ProfileDetailView.as_view(), name='profile_detail'),
]
