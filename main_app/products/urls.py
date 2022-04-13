from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_user, name="login_user"),
    path('logout/',views.logout_user, name="logout_user"),
    path("products/", views.ProductsView.as_view(), name="products"),
    path("nutrition/", views.nutrition, name="nutrition"),
]