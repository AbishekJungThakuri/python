from django.urls import path
from .views import CarViewset

urlpatterns = [
    path('car/', CarViewset.as_view()),
    path('car/<int:id>',CarViewset.as_view())
]