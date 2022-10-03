from django.urls import path

from bot import views
urlpatterns = [
    path('', views.webhook),
    path('webhook/', views.webhook),
]
