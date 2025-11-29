from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Count, Avg, Q, F
from .models import StudentSurvey, TeacherSurvey


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_filtered_analytics(request):
    """
    Get analytics data with multi-dimensional filtering
    Query params: gender, age_range, min_price, max_price, frequency, session_length, platform_interest
    """
    # Get filter parameters
    gender = request.query_params.get('gender')
    age_range = request.query_params.get('age_range')
    min_price = request.query_params.get('min_price')
    max_price = request.query_params.get('max_price')
    frequency = request.query_params.get('frequency')
    session_length = request.query_params.get('session_length')
    platform_interest = request.query_params.get('platform_interest')  # 'willing', 'not_willing'
    
    # Build query for students
    student_query = Q()
    if gender:
        student_query &= Q(gender=gender)
    if age_range:
        student_query &= Q(age_range=age_range)
    if min_price:
        student_query &= Q(fair_price_etb__gte=float(min_price))
    if max_price:
        student_query &= Q(fair_price_etb__lte=float(max_price))
    if frequency:
        student_query &= Q(preferred_frequency=frequency)
    if session_length:
        student_query &= Q(preferred_session_length=int(session_length))
    if platform_interest == 'willing':
        student_query &= Q(willing_to_try=True)
    elif platform_interest == 'not_willing':
        student_query &= Q(willing_to_try=False)
    
    students = StudentSurvey.objects.filter(student_query)
    
    # Build query for teachers
    teacher_query = Q()
    if gender:
        teacher_query &= Q(gender=gender)
    if age_range:
        teacher_query &= Q(age_range=age_range)
    if min_price:
        teacher_query &= Q(fair_rate_etb__gte=float(min_price))
    if max_price:
        teacher_query &= Q(fair_rate_etb__lte=float(max_price))
    if session_length:
        teacher_query &= Q(preferred_session_length=int(session_length))
    if platform_interest == 'willing':
        teacher_query &= Q(would_join_platform=True)
    elif platform_interest == 'not_willing':
        teacher_query &= Q(would_join_platform=False)
    
    teachers = TeacherSurvey.objects.filter(teacher_query)
    
    # Calculate analytics
    total_students = students.count()
    total_teachers = teachers.count()
    
    # Gender distribution
    gender_dist = students.values('gender').annotate(count=Count('id'))
    
    # Age distribution
    age_dist = students.values('age_range').annotate(count=Count('id'))
    
    # Session length preferences
    session_dist = students.values('preferred_session_length').annotate(count=Count('id'))
    
    # Frequency preferences
    frequency_dist = students.values('preferred_frequency').annotate(count=Count('id'))
    
    # Platform interest
    student_willing = students.filter(willing_to_try=True).count()
    student_not_willing = students.filter(willing_to_try=False).count()
    
    teacher_willing = teachers.filter(would_join_platform=True).count()
    teacher_not_willing = teachers.filter(would_join_platform=False).count()
    
    # Average price
    avg_student_price = students.aggregate(avg=Avg('fair_price_etb'))['avg'] or 0
    avg_teacher_rate = teachers.aggregate(avg=Avg('fair_rate_etb'))['avg'] or 0
    
    # Cross-dimensional analysis: Age × Gender
    age_gender_matrix = []
    age_ranges = ['8-15', '15-24', '24-32', '32-40', '40+']
    genders = ['male', 'female']
    
    for age in age_ranges:
        for gen in genders:
            count = students.filter(age_range=age, gender=gen).count()
            if count > 0:  # Only include non-zero counts
                age_gender_matrix.append({
                    'age_range': age,
                    'gender': gen,
                    'count': count
                })
    
    # Price × Session Length heatmap data
    price_ranges = [
        {'min': 0, 'max': 100, 'label': '0-100'},
        {'min': 100, 'max': 200, 'label': '100-200'},
        {'min': 200, 'max': 300, 'label': '200-300'},
        {'min': 300, 'max': 999999, 'label': '300+'}
    ]
    session_lengths = [20, 30, 45, 60]
    
    price_session_matrix = []
    for price_range in price_ranges:
        for session_len in session_lengths:
            count = students.filter(
                fair_price_etb__gte=price_range['min'],
                fair_price_etb__lt=price_range['max'],
                preferred_session_length=session_len
            ).count()
            if count > 0:
                price_session_matrix.append({
                    'price_range': price_range['label'],
                    'session_length': session_len,
                    'count': count
                })
    
    return Response({
        'total_students': total_students,
        'total_teachers': total_teachers,
        'filters_applied': {
            'gender': gender,
            'age_range': age_range,
            'min_price': min_price,
            'max_price': max_price,
            'frequency': frequency,
            'session_length': session_length,
            'platform_interest': platform_interest
        },
        'gender_distribution': list(gender_dist),
        'age_distribution': list(age_dist),
        'session_distribution': list(session_dist),
        'frequency_distribution': list(frequency_dist),
        'platform_interest': {
            'students': {
                'willing': student_willing,
                'not_willing': student_not_willing
            },
            'teachers': {
                'willing': teacher_willing,
                'not_willing': teacher_not_willing
            }
        },
        'average_prices': {
            'student_price': round(avg_student_price, 2),
            'teacher_rate': round(avg_teacher_rate, 2)
        },
        'age_gender_matrix': age_gender_matrix,
        'price_session_matrix': price_session_matrix
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_list(request):
    """
    Get paginated user list with filtering (both students and teachers)
    Query params: user_type, gender, age_range, min_price, max_price, frequency, session_length, search, page, page_size
    """
    # Get filter and pagination parameters
    user_type = request.query_params.get('user_type', 'all')  # 'student', 'teacher', or 'all'
    gender = request.query_params.get('gender')
    age_range = request.query_params.get('age_range')
    min_price = request.query_params.get('min_price')
    max_price = request.query_params.get('max_price')
    frequency = request.query_params.get('frequency')
    session_length = request.query_params.get('session_length')
    search = request.query_params.get('search', '')
    page = int(request.query_params.get('page', 1))
    page_size = int(request.query_params.get('page_size', 50))
    
    users = []
    
    # Fetch students if requested
    if user_type in ['all', 'student']:
        query = Q()
        if gender:
            query &= Q(gender=gender)
        if age_range:
            query &= Q(age_range=age_range)
        if min_price:
            query &= Q(fair_price_etb__gte=float(min_price))
        if max_price:
            query &= Q(fair_price_etb__lte=float(max_price))
        if frequency:
            query &= Q(preferred_frequency=frequency)
        if session_length:
            query &= Q(preferred_session_length=int(session_length))
        if search:
            query &= Q(Q(full_name__icontains=search) | Q(phone_number__icontains=search))
        
        students = StudentSurvey.objects.filter(query).order_by('-submitted_at')
        
        for student in students:
            users.append({
                'id': f"student_{student.id}",
                'type': 'student',
                'name': student.full_name,
                'phone': student.phone_number,
                'gender': student.gender,
                'age_range': student.age_range,
                'session_length': student.preferred_session_length,
                'frequency': student.preferred_frequency,
                'price': student.fair_price_etb,
                'platform_interest': student.willing_to_try,
                'subjects': student.subjects_of_interest if student.subjects_of_interest else [],
                'submitted_at': student.submitted_at.isoformat() if student.submitted_at else None
            })
    
    # Fetch teachers if requested
    if user_type in ['all', 'teacher']:
        query = Q()
        if gender:
            query &= Q(gender=gender)
        if age_range:
            query &= Q(age_range=age_range)
        if min_price:
            query &= Q(fair_rate_etb__gte=float(min_price))
        if max_price:
            query &= Q(fair_rate_etb__lte=float(max_price))
        if session_length:
            query &= Q(preferred_session_length=int(session_length))
        if search:
            query &= Q(Q(full_name__icontains=search) | Q(phone_number__icontains=search))
        
        teachers = TeacherSurvey.objects.filter(query).order_by('-submitted_at')
        
        for teacher in teachers:
            users.append({
                'id': f"teacher_{teacher.id}",
                'type': 'teacher',
                'name': teacher.full_name,
                'phone': teacher.phone_number,
                'gender': teacher.gender,
                'age_range': teacher.age_range,
                'session_length': teacher.preferred_session_length,
                'frequency': None,  # Teachers don't have frequency
                'price': teacher.fair_rate_etb,
                'platform_interest': teacher.would_join_platform,
                'subjects': teacher.confident_topics if teacher.confident_topics else [],
                'submitted_at': teacher.submitted_at.isoformat() if teacher.submitted_at else None
            })
    
    # Sort all users by submitted_at (most recent first)
    users.sort(key=lambda x: x['submitted_at'] or '', reverse=True)
    
    # Pagination
    total = len(users)
    start = (page - 1) * page_size
    end = start + page_size
    paginated_users = users[start:end]
    
    return Response({
        'total': total,
        'page': page,
        'page_size': page_size,
        'total_pages': (total + page_size - 1) // page_size if total > 0 else 0,
        'users': paginated_users
    })

