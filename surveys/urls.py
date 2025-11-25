from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'student', views.StudentSurveyViewSet, basename='student-survey')
router.register(r'teacher', views.TeacherSurveyViewSet, basename='teacher-survey')

urlpatterns = [
    path('surveys/', include(router.urls)),
    path('analytics/students/', views.student_analytics, name='student-analytics'),
    path('analytics/teachers/', views.teacher_analytics, name='teacher-analytics'),
    path('analytics/summary/', views.analytics_summary, name='analytics-summary'),
]
