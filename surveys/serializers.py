from rest_framework import serializers
from .models import StudentSurvey, TeacherSurvey


class StudentSurveySerializer(serializers.ModelSerializer):
    """Serializer for StudentSurvey model"""

    class Meta:
        model = StudentSurvey
        fields = [
            'id',
            'full_name',
            'age_range',
            'phone_number',
            'quran_experience',
            'taken_online_lessons',
            'online_lessons_reason',
            'teacher_challenges',
            'time_preference',
            'preferred_session_length',
            'preferred_frequency',
            'fair_price_etb',
            'subjects_of_interest',
            'trust_factors',
            'willing_to_try',
            'willing_to_try_reason',
            'desired_features',
            'submitted_at',
            'ip_address',
        ]
        read_only_fields = ['id', 'submitted_at', 'ip_address']
        extra_kwargs = {
            'phone_number': {'allow_blank': False, 'allow_null': False}
        }

    def validate_full_name(self, value: str) -> str:
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Full name is required.")
        if len(value) < 3:
            raise serializers.ValidationError("Full name must be at least 3 characters long.")
        return value

    def validate_phone_number(self, value: str) -> str:
        """Normalize and validate Ethiopian phone numbers"""
        value = value.strip()

        if value.startswith('0'):
            value = value[1:]

        if not value.startswith('+251'):
            value = '+251' + value

        if len(value) != 13:
            raise serializers.ValidationError("Invalid phone number length. Must be 9 digits (e.g., 911223344).")

        if value[4] not in ['9', '7']:
            raise serializers.ValidationError("Invalid phone number. Must start with 9 or 7 (e.g., 09... or 07...).")

        if not value[1:].isdigit():
            raise serializers.ValidationError("Phone number must contain only digits.")

        return value

    def validate_subjects_of_interest(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Subjects of interest must be a list")
        return value

    def validate_fair_price_etb(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be a positive number")
        return value


class TeacherSurveySerializer(serializers.ModelSerializer):
    """Serializer for TeacherSurvey model"""

    class Meta:
        model = TeacherSurvey
        fields = [
            'id',
            'full_name',
            'age_range',
            'phone_number',
            'teaching_background',
            'teaching_background_details',
            'tried_online_teaching',
            'online_teaching_reason',
            'teaching_challenges',
            'students_per_week',
            'preferred_session_length',
            'fair_rate_etb',
            'confident_topics',
            'would_join_platform',
            'support_needed',
            'platform_concerns',
            'feedback_preferences',
            'wants_early_access',
            'early_access_contact',
            'submitted_at',
            'ip_address',
        ]
        read_only_fields = ['id', 'submitted_at', 'ip_address']

    def validate_full_name(self, value: str) -> str:
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Full name is required.")
        if len(value) < 3:
            raise serializers.ValidationError("Full name must be at least 3 characters long.")
        return value

    def validate_phone_number(self, value: str) -> str:
        value = value.strip()

        if value.startswith('0'):
            value = value[1:]

        if not value.startswith('+251'):
            value = '+251' + value

        if len(value) != 13:
            raise serializers.ValidationError("Invalid phone number length. Must be 9 digits (e.g., 911223344).")

        if value[4] not in ['9', '7']:
            raise serializers.ValidationError("Invalid phone number. Must start with 9 or 7 (e.g., 09... or 07...).")

        if not value[1:].isdigit():
            raise serializers.ValidationError("Phone number must contain only digits.")

        return value

    def validate_confident_topics(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Confident topics must be a list")
        return value

    def validate_students_per_week(self, value):
        if value < 0:
            raise serializers.ValidationError("Number of students must be positive")
        return value

    def validate_fair_rate_etb(self, value):
        if value < 0:
            raise serializers.ValidationError("Rate must be a positive number")
        return value
