from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count, Avg, Q
from .models import StudentSurvey, TeacherSurvey
from .serializers import StudentSurveySerializer, TeacherSurveySerializer


class StudentSurveyViewSet(viewsets.ModelViewSet):
    """ViewSet for student survey submissions"""
    queryset = StudentSurvey.objects.all()
    serializer_class = StudentSurveySerializer
    http_method_names = ['get', 'post', 'head', 'options']
    
    def perform_create(self, serializer):
        # Capture IP address
        ip = self.request.META.get('REMOTE_ADDR')
        serializer.save(ip_address=ip)


class TeacherSurveyViewSet(viewsets.ModelViewSet):
    """ViewSet for teacher survey submissions"""
    queryset = TeacherSurvey.objects.all()
    serializer_class = TeacherSurveySerializer
    http_method_names = ['get', 'post', 'head', 'options']
    
    def perform_create(self, serializer):
        # Capture IP address
        ip = self.request.META.get('REMOTE_ADDR')
        serializer.save(ip_address=ip)


@api_view(['GET'])
def student_analytics(request):
    """Get analytics data for student surveys"""
    total_count = StudentSurvey.objects.count()
    
    # Experience level distribution
    experience_data = StudentSurvey.objects.values('quran_experience').annotate(
        count=Count('id')
    ).order_by('quran_experience')
    
    # Session length preferences
    session_length_data = StudentSurvey.objects.values('preferred_session_length').annotate(
        count=Count('id')
    ).order_by('preferred_session_length')
    
    # Frequency preferences
    frequency_data = StudentSurvey.objects.values('preferred_frequency').annotate(
        count=Count('id')
    ).order_by('preferred_frequency')
    
    # Time preferences
    time_data = StudentSurvey.objects.values('time_preference').annotate(
        count=Count('id')
    ).order_by('time_preference')
    
    # Willingness to try
    willing_count = StudentSurvey.objects.filter(willing_to_try=True).count()
    not_willing_count = StudentSurvey.objects.filter(willing_to_try=False).count()
    
    # Online lessons experience
    online_yes = StudentSurvey.objects.filter(taken_online_lessons=True).count()
    online_no = StudentSurvey.objects.filter(taken_online_lessons=False).count()
    
    # Average price
    avg_price = StudentSurvey.objects.aggregate(Avg('fair_price_etb'))['fair_price_etb__avg']
    
    # Subjects interest aggregation
    all_subjects = []
    for survey in StudentSurvey.objects.all():
        if survey.subjects_of_interest:
            all_subjects.extend(survey.subjects_of_interest)
    
    from collections import Counter
    subject_counts = Counter(all_subjects)
    subjects_data = [{'subject': k, 'count': v} for k, v in subject_counts.items()]
    
    return Response({
        'total_responses': total_count,
        'experience_distribution': list(experience_data),
        'session_length_distribution': list(session_length_data),
        'frequency_distribution': list(frequency_data),
        'time_preference_distribution': list(time_data),
        'willingness': {
            'willing': willing_count,
            'not_willing': not_willing_count
        },
        'online_experience': {
            'yes': online_yes,
            'no': online_no
        },
        'average_price': round(float(avg_price) if avg_price else 0, 2),
        'subjects_interest': subjects_data
    })


@api_view(['GET'])
def teacher_analytics(request):
    """Get analytics data for teacher surveys"""
    total_count = TeacherSurvey.objects.count()
    
    # Teaching background distribution
    background_data = TeacherSurvey.objects.values('teaching_background').annotate(
        count=Count('id')
    ).order_by('teaching_background')
    
    # Session length preferences
    session_length_data = TeacherSurvey.objects.values('preferred_session_length').annotate(
        count=Count('id')
    ).order_by('preferred_session_length')
    
    # Platform interest
    would_join = TeacherSurvey.objects.filter(would_join_platform=True).count()
    would_not_join = TeacherSurvey.objects.filter(would_join_platform=False).count()
    
    # Online teaching experience
    tried_online = TeacherSurvey.objects.filter(tried_online_teaching=True).count()
    not_tried_online = TeacherSurvey.objects.filter(tried_online_teaching=False).count()
    
    # Early access interest
    wants_early = TeacherSurvey.objects.filter(wants_early_access=True).count()
    
    # Average metrics
    avg_students = TeacherSurvey.objects.aggregate(Avg('students_per_week'))['students_per_week__avg']
    avg_rate = TeacherSurvey.objects.aggregate(Avg('fair_rate_etb'))['fair_rate_etb__avg']
    
    # Topics confidence aggregation
    all_topics = []
    for survey in TeacherSurvey.objects.all():
        if survey.confident_topics:
            all_topics.extend(survey.confident_topics)
    
    from collections import Counter
    topic_counts = Counter(all_topics)
    topics_data = [{'topic': k, 'count': v} for k, v in topic_counts.items()]
    
    return Response({
        'total_responses': total_count,
        'teaching_background_distribution': list(background_data),
        'session_length_distribution': list(session_length_data),
        'platform_interest': {
            'would_join': would_join,
            'would_not_join': would_not_join
        },
        'online_experience': {
            'tried': tried_online,
            'not_tried': not_tried_online
        },
        'early_access_interest': wants_early,
        'average_students_per_week': round(float(avg_students) if avg_students else 0, 1),
        'average_rate': round(float(avg_rate) if avg_rate else 0, 2),
        'confident_topics': topics_data
    })


@api_view(['GET'])
def analytics_summary(request):
    """Get overall summary of both surveys"""
    student_count = StudentSurvey.objects.count()
    teacher_count = TeacherSurvey.objects.count()
    
    last_student = StudentSurvey.objects.order_by('-submitted_at').first()
    last_teacher = TeacherSurvey.objects.order_by('-submitted_at').first()
    
    last_updated = None
    if last_student and last_teacher:
        last_updated = max(last_student.submitted_at, last_teacher.submitted_at)
    elif last_student:
        last_updated = last_student.submitted_at
    elif last_teacher:
        last_updated = last_teacher.submitted_at
    
    return Response({
        'total_student_responses': student_count,
        'total_teacher_responses': teacher_count,
        'total_responses': student_count + teacher_count,
        'last_updated': last_updated
    })
