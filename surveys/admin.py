from django.contrib import admin
from .models import StudentSurvey, TeacherSurvey


@admin.register(StudentSurvey)
class StudentSurveyAdmin(admin.ModelAdmin):
    """Admin interface for student surveys"""
    list_display = [
        'id',
        'quran_experience',
        'willing_to_try',
        'preferred_session_length',
        'fair_price_etb',
        'submitted_at'
    ]
    list_filter = [
        'quran_experience',
        'willing_to_try',
        'taken_online_lessons',
        'preferred_session_length',
        'preferred_frequency',
        'time_preference',
        'submitted_at'
    ]
    search_fields = [
        'teacher_challenges',
        'trust_factors',
        'desired_features',
        'online_lessons_reason'
    ]
    readonly_fields = ['submitted_at', 'ip_address']
    date_hierarchy = 'submitted_at'
    ordering = ['-submitted_at']
    
    fieldsets = (
        ('Experience & Background', {
            'fields': ('quran_experience', 'taken_online_lessons', 'online_lessons_reason', 'teacher_challenges')
        }),
        ('Preferences', {
            'fields': ('time_preference', 'preferred_session_length', 'preferred_frequency', 'fair_price_etb', 'subjects_of_interest')
        }),
        ('Platform Interest', {
            'fields': ('trust_factors', 'willing_to_try', 'willing_to_try_reason', 'desired_features')
        }),
        ('Metadata', {
            'fields': ('submitted_at', 'ip_address'),
            'classes': ('collapse',)
        }),
    )


@admin.register(TeacherSurvey)
class TeacherSurveyAdmin(admin.ModelAdmin):
    """Admin interface for teacher surveys"""
    list_display = [
        'id',
        'teaching_background',
        'would_join_platform',
        'students_per_week',
        'fair_rate_etb',
        'wants_early_access',
        'submitted_at'
    ]
    list_filter = [
        'teaching_background',
        'would_join_platform',
        'tried_online_teaching',
        'wants_early_access',
        'preferred_session_length',
        'submitted_at'
    ]
    search_fields = [
        'teaching_background_details',
        'teaching_challenges',
        'support_needed',
        'platform_concerns',
        'feedback_preferences',
        'early_access_contact'
    ]
    readonly_fields = ['submitted_at', 'ip_address']
    date_hierarchy = 'submitted_at'
    ordering = ['-submitted_at']
    
    fieldsets = (
        ('Teaching Background', {
            'fields': ('teaching_background', 'teaching_background_details', 'tried_online_teaching', 'online_teaching_reason')
        }),
        ('Current Situation', {
            'fields': ('teaching_challenges', 'students_per_week', 'preferred_session_length', 'fair_rate_etb', 'confident_topics')
        }),
        ('Platform Interest', {
            'fields': ('would_join_platform', 'support_needed', 'platform_concerns', 'feedback_preferences')
        }),
        ('Early Access', {
            'fields': ('wants_early_access', 'early_access_contact')
        }),
        ('Metadata', {
            'fields': ('submitted_at', 'ip_address'),
            'classes': ('collapse',)
        }),
    )
