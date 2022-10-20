from django.urls import path

from . import views

urlpatterns = [
    # already /api/products/
    path('', views.product_list_create_view),
    path('<int:pk>/', views.product_create_view)
]