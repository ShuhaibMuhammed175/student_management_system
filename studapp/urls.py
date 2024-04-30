from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('all_students/', views.all_students.as_view()),
    path('student_update/<int:pk>/', views.StudentUpdateAPIView.as_view()),
    path('add/student/', views.AddStudentAPIView.as_view()),
    path('student/detail/<int:pk>/', views.StudentDetailAPIView.as_view()),
    path('student/delete/<int:pk>/', views.StudentDeleteAPIView.as_view()),
]