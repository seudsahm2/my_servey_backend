from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db.models import Count, Q, Avg
from .models import StudentSurvey, TeacherSurvey, SurveyQuestion
from .serializers import StudentSurveySerializer, TeacherSurveySerializer, SurveyQuestionSerializer
from .defaults import DEFAULT_STUDENT_QUESTIONS, DEFAULT_TEACHER_QUESTIONS
from rest_framework import serializers
import logging

logger = logging.getLogger(__name__)


class StudentSurveyViewSet(viewsets.ModelViewSet):
    """ViewSet for student survey submissions"""
    queryset = StudentSurvey.objects.all()
    serializer_class = StudentSurveySerializer
    http_method_names = ['get', 'post', 'head', 'options']
    permission_classes = [AllowAny]  # Allow public access for survey submissions
    authentication_classes = []  # Disable JWT authentication - surveys are public!
    
    def perform_create(self, serializer):
        # Capture IP address
        ip = self.request.META.get('REMOTE_ADDR')
        serializer.save(ip_address=ip)

    @action(detail=False, methods=['get'], url_path='check-phone', permission_classes=[AllowAny])
    def check_phone(self, request):
        logger.info(f"[STUDENT_CHECK_PHONE] Endpoint called")
        logger.debug(f"[STUDENT_CHECK_PHONE] Headers: {dict(request.headers)}")
        logger.debug(f"[STUDENT_CHECK_PHONE] User: {request.user}, Authenticated: {request.user.is_authenticated}")
        logger.debug(f"[STUDENT_CHECK_PHONE] Permission classes: {self.permission_classes}")
        
        phone = request.query_params.get('phone', '')
        logger.info(f"[STUDENT_CHECK_PHONE] Phone parameter: {phone}")
        
        serializer = self.get_serializer()
        if not phone:
            logger.warning("[STUDENT_CHECK_PHONE] Phone number missing")
            return Response(
                {'valid': False, 'exists': False, 'error': ['Phone number is required.']},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            normalized = serializer.validate_phone_number(phone)
            logger.debug(f"[STUDENT_CHECK_PHONE] Normalized phone: {normalized}")
        except serializers.ValidationError as exc:  # type: ignore[name-defined]
            logger.warning(f"[STUDENT_CHECK_PHONE] Validation error: {exc.detail}")
            return Response({'valid': False, 'exists': False, 'error': exc.detail}, status=status.HTTP_400_BAD_REQUEST)

        exists = StudentSurvey.objects.filter(phone_number=normalized).exists()
        logger.info(f"[STUDENT_CHECK_PHONE] Phone exists: {exists}")
        return Response({'valid': True, 'exists': exists})


class TeacherSurveyViewSet(viewsets.ModelViewSet):
    """ViewSet for teacher survey submissions"""
    queryset = TeacherSurvey.objects.all()
    serializer_class = TeacherSurveySerializer
    http_method_names = ['get', 'post', 'head', 'options']
    permission_classes = [AllowAny]  # Allow public access for survey submissions
    authentication_classes = []  # Disable JWT authentication - surveys are public!
    
    def perform_create(self, serializer):
        # Capture IP address
        ip = self.request.META.get('REMOTE_ADDR')
        serializer.save(ip_address=ip)

    @action(detail=False, methods=['get'], url_path='check-phone', permission_classes=[AllowAny])
    def check_phone(self, request):
        logger.info(f"[TEACHER_CHECK_PHONE] Endpoint called")
        logger.debug(f"[TEACHER_CHECK_PHONE] Headers: {dict(request.headers)}")
        logger.debug(f"[TEACHER_CHECK_PHONE] User: {request.user}, Authenticated: {request.user.is_authenticated}")
        logger.debug(f"[TEACHER_CHECK_PHONE] Permission classes: {self.permission_classes}")
        
        phone = request.query_params.get('phone', '')
        logger.info(f"[TEACHER_CHECK_PHONE] Phone parameter: {phone}")
        
        serializer = self.get_serializer()
        if not phone:
            logger.warning("[TEACHER_CHECK_PHONE] Phone number missing")
            return Response(
                {'valid': False, 'exists': False, 'error': ['Phone number is required.']},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            normalized = serializer.validate_phone_number(phone)
            logger.debug(f"[TEACHER_CHECK_PHONE] Normalized phone: {normalized}")
        except serializers.ValidationError as exc:  # type: ignore[name-defined]
            logger.warning(f"[TEACHER_CHECK_PHONE] Validation error: {exc.detail}")
            return Response({'valid': False, 'exists': False, 'error': exc.detail}, status=status.HTTP_400_BAD_REQUEST)

        exists = TeacherSurvey.objects.filter(phone_number=normalized).exists()
        logger.info(f"[TEACHER_CHECK_PHONE] Phone exists: {exists}")
        return Response({'valid': True, 'exists': exists})


class SurveyQuestionViewSet(viewsets.ModelViewSet):
    """ViewSet for managing survey questions"""
    queryset = SurveyQuestion.objects.all()
    serializer_class = SurveyQuestionSerializer
    filterset_fields = ['survey_type', 'section', 'is_active']
    permission_classes = [AllowAny]  # You can change this based on your requirements

    @action(detail=False, methods=['post'])
    def reset(self, request):
        """Reset questions to default for a specific survey type"""
        survey_type = request.data.get('survey_type')
        if survey_type not in ['student', 'teacher']:
            return Response(
                {'error': 'Invalid or missing survey_type. Must be "student" or "teacher".'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Delete existing questions for this type
        SurveyQuestion.objects.filter(survey_type=survey_type).delete()

        # Load defaults
        defaults = DEFAULT_STUDENT_QUESTIONS if survey_type == 'student' else DEFAULT_TEACHER_QUESTIONS
        
        created_count = 0
        for section, questions in defaults.items():
            for q_data in questions:
                SurveyQuestion.objects.create(
                    survey_type=survey_type,
                    section=section,
                    identifier=q_data['identifier'],
                    text_en=q_data['text_en'],
                    text_ar=q_data['text_ar'],
                    question_type=q_data.get('type', 'choice'),
                    options_en=q_data.get('options_en', []),
                    options_ar=q_data.get('options_ar', []),
                    order=created_count
                )
                created_count += 1

        return Response({
            'message': f'Reset {created_count} questions for {survey_type} survey',
            'count': created_count
        }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def student_analytics(request):
    """Get analytics data for student surveys"""
    logger.info(f"[STUDENT_ANALYTICS] Endpoint called")
    logger.debug(f"[STUDENT_ANALYTICS] Headers: {dict(request.headers)}")
    logger.debug(f"[STUDENT_ANALYTICS] User: {request.user}, Authenticated: {request.user.is_authenticated}")
    logger.debug(f"[STUDENT_ANALYTICS] Permission decorators: IsAuthenticated")
    
    total_count = StudentSurvey.objects.count()
    logger.info(f"[STUDENT_ANALYTICS] Total student surveys: {total_count}")
    
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
    
    # Count subjects
    subjects_data = {}
    for subject in all_subjects:
        subjects_data[subject] = subjects_data.get(subject, 0) + 1

    # Age distribution
    age_data = StudentSurvey.objects.values('age_range').annotate(
        count=Count('id')
    ).order_by('age_range')

    # Age vs Subjects
    age_subjects = {}
    for survey in StudentSurvey.objects.all():
        age = survey.age_range
        if age not in age_subjects:
            age_subjects[age] = {}
        if survey.subjects_of_interest:
            for subject in survey.subjects_of_interest:
                age_subjects[age][subject] = age_subjects[age].get(subject, 0) + 1
    
    return Response({
        'total_responses': total_count,
        'experience_distribution': list(experience_data),
        'session_length_preferences': list(session_length_data),
        'frequency_preferences': list(frequency_data),
        'time_preferences': list(time_data),
        'willingness_to_try': {
            'willing': willing_count,
            'not_willing': not_willing_count
        },
        'online_experience': {
            'yes': online_yes,
            'no': online_no
        },
        'average_price': round(float(avg_price) if avg_price else 0, 2),
        'subjects_interest': subjects_data,
        'age_distribution': list(age_data),
        'age_subjects_interest': age_subjects
    })


@api_view(['GET'])
def teacher_analytics(request):
    """Get analytics data for teacher surveys"""
    logger.info(f"[TEACHER_ANALYTICS] Endpoint called")
    logger.debug(f"[TEACHER_ANALYTICS] Headers: {dict(request.headers)}")
    logger.debug(f"[TEACHER_ANALYTICS] User: {request.user}, Authenticated: {request.user.is_authenticated}")
    logger.debug(f"[TEACHER_ANALYTICS] Permission decorators: NONE (missing @permission_classes)")
    
    total_count = TeacherSurvey.objects.count()
    logger.info(f"[TEACHER_ANALYTICS] Total teacher surveys: {total_count}")
    
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
    
    # Count topics
    topics_data = {}
    for topic in all_topics:
        topics_data[topic] = topics_data.get(topic, 0) + 1

    # Age distribution
    age_data = TeacherSurvey.objects.values('age_range').annotate(
        count=Count('id')
    ).order_by('age_range')
    
    return Response({
        'total_responses': total_count,
        'background_distribution': list(background_data),
        'session_length_preferences': list(session_length_data),
        'platform_interest': {
            'would_join': would_join,
            'would_not_join': would_not_join
        },
        'online_teaching_experience': {
            'tried': tried_online,
            'not_tried': not_tried_online
        },
        'early_access_interest': wants_early,
        'average_students_per_week': round(float(avg_students) if avg_students else 0, 1),
        'average_rate': round(float(avg_rate) if avg_rate else 0, 2),
        'confident_topics': topics_data,
        'age_distribution': list(age_data)
    })


@api_view(['GET'])
def analytics_summary(request):
    """Get overall summary of both surveys"""
    logger.info(f"[ANALYTICS_SUMMARY] Endpoint called")
    logger.debug(f"[ANALYTICS_SUMMARY] Headers: {dict(request.headers)}")
    logger.debug(f"[ANALYTICS_SUMMARY] User: {request.user}, Authenticated: {request.user.is_authenticated}")
    logger.debug(f"[ANALYTICS_SUMMARY] Permission decorators: NONE (missing @permission_classes)")
    
    student_count = StudentSurvey.objects.count()
    teacher_count = TeacherSurvey.objects.count()
    logger.info(f"[ANALYTICS_SUMMARY] Student count: {student_count}, Teacher count: {teacher_count}")
    
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
