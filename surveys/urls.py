from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentSurveyViewSet, TeacherSurveyViewSet, SurveyQuestionViewSet, student_analytics, teacher_analytics, analytics_summary
from .analytics_views import get_filtered_analytics, get_user_list

router = DefaultRouter()
router.register(r'student-surveys', StudentSurveyViewSet, basename='student-survey')
router.register(r'teacher-surveys', TeacherSurveyViewSet, basename='teacher-survey')
router.register(r'questions', SurveyQuestionViewSet, basename='survey-questions')

urlpatterns = [
    # ViewSet routes
    path('', include(router.urls)),
    
    # Analytics endpoints
    path('analytics/students/', student_analytics, name='student-analytics'),
    path('analytics/teachers/', teacher_analytics, name='teacher-analytics'),
    path('analytics/summary/', analytics_summary, name='analytics-summary'),
    path('analytics/filtered/', get_filtered_analytics, name='filtered-analytics'),
    
    # User management endpoint
    path('users/list/', get_user_list, name='user-list'),
]
