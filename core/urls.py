from django.urls import path
from core.views import contador

urlpatterns = [
    path("contador/", contador, name="contador"),
]
