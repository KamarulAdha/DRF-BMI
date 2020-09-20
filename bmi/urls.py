from django.urls import path, include

from bmi import views

urlpatterns = [
    path('bmi/', views.BMICalculatorAPIView.as_view()),
]
