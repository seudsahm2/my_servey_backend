from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class StudentSurvey(models.Model):
    """Model for student interview survey responses"""
    
    EXPERIENCE_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    
    SESSION_LENGTH_CHOICES = [
        (20, '20 minutes'),
        (30, '30 minutes'),
        (45, '45 minutes'),
        (60, '60 minutes'),
    ]
    
    FREQUENCY_CHOICES = [
        ('once_week', 'Once a week'),
        ('twice_week', 'Twice a week'),
        ('more', 'More than twice a week'),
    ]
    
    TIME_PREFERENCE_CHOICES = [
        ('mornings', 'Mornings'),
        ('evenings', 'Evenings'),
        ('weekends', 'Weekends'),
        ('flexible', 'Flexible'),
    ]
    
    AGE_RANGE_CHOICES = [
        ('8-15', '8-15'),
        ('15-24', '15-24'),
        ('24-32', '24-32'),
        ('32-40', '32-40'),
        ('40+', '40+'),
    ]
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    full_name = models.CharField(
        max_length=255,
        blank=False,
        default='',
        help_text="Full name of the student"
    )

    age_range = models.CharField(
        max_length=10,
        choices=AGE_RANGE_CHOICES,
        default='15-24',
        help_text="Age range of the student"
    )

    # Q0: Phone Number (Identity)
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        blank=True,
        help_text="Phone number for identity verification (e.g., +251...)"
    )
    
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        default='male',
        help_text="Gender"
    )

    # Q1: Current experience reading the Quran (Optional - only for Quran students)
    quran_experience = models.CharField(
        max_length=20,
        choices=EXPERIENCE_CHOICES,
        blank=True,
        null=True,
        help_text="What is your current experience reading the Quran?"
    )

    # Q2: Have you ever taken Quran lessons online?
    taken_online_lessons = models.BooleanField(
        help_text="Have you ever taken Quran lessons online?"
    )
    online_lessons_reason = models.TextField(
        blank=True,
        help_text="Why or why not?"
    )
    
    # Q3: Challenges in finding a qualified teacher
    teacher_challenges = models.TextField(
        help_text="What challenges do you face in finding a qualified teacher?"
    )
    
    # Q4: Free time availability
    time_preference = models.CharField(
        max_length=20,
        choices=TIME_PREFERENCE_CHOICES,
        help_text="When do you generally have free time to study?"
    )
    
    # Q5: Preferred session length
    preferred_session_length = models.IntegerField(
        choices=SESSION_LENGTH_CHOICES,
        help_text="How many minutes per session do you prefer?"
    )
    
    # Q6: Preferred frequency
    preferred_frequency = models.CharField(
        max_length=20,
        choices=FREQUENCY_CHOICES,
        help_text="How often would you like to have sessions?"
    )
    
    # Q7: Fair price for session in ETB
    fair_price_etb = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text="What is a fair price for a session in ETB?"
    )
    
    # Q8: Subjects of interest (stored as JSON array)
    subjects_of_interest = models.JSONField(
        help_text="Which subjects interest you most? (Quran reading, Tajweed, Hadith, Arabic, Islamic arts)"
    )
    
    # Q9: What builds trust in online teacher
    trust_factors = models.TextField(
        help_text="What would make you trust an online teacher? (Ratings, verification, community)"
    )
    
    # Q10: Willingness to try the platform
    willing_to_try = models.BooleanField(
        help_text="If such a platform existed, would you be willing to try it?"
    )
    willing_to_try_reason = models.TextField(
        blank=True,
        help_text="Why or why not?"
    )

    desired_features = models.TextField(
        blank=True,
        help_text="What features would you like to see?"
    )

    # Dynamic responses
    dynamic_responses = models.JSONField(
        default=dict,
        blank=True,
        help_text="Responses to dynamic questions based on interests"
    )

    submitted_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"Student Survey - {self.submitted_at.strftime('%Y-%m-%d %H:%M')}"


class TeacherSurvey(models.Model):
    """Model for teacher (Ustaz) interview survey responses"""
    
    TEACHING_BACKGROUND_CHOICES = [
        ('madrasa', 'Madrasa'),
        ('mosque', 'Mosque'),
        ('private', 'Private'),
        ('online', 'Online'),
        ('mixed', 'Mixed'),
    ]
    
    SESSION_LENGTH_CHOICES = [
        (20, '20 minutes'),
        (30, '30 minutes'),
        (45, '45 minutes'),
        (60, '60 minutes'),
    ]

    AGE_RANGE_CHOICES = [
        ('8-15', '8-15'),
        ('15-24', '15-24'),
        ('24-32', '24-32'),
        ('32-40', '32-40'),
        ('40+', '40+'),
    ]
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    
    full_name = models.CharField(
        max_length=255,
        blank=False,
        default='',
        help_text="Full name of the teacher"
    )

    age_range = models.CharField(
        max_length=10,
        choices=AGE_RANGE_CHOICES,
        default='24-32',
        help_text="Age range of the teacher"
    )

    phone_number = models.CharField(
        max_length=15,
        unique=True,
        help_text="Phone number for identity verification (e.g., +251...)"
    )
    
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        default='male',
        help_text="Gender"
    )

    teaching_background = models.CharField(
        max_length=20,
        choices=TEACHING_BACKGROUND_CHOICES,
        help_text="What is your teaching background?"
    )
    teaching_background_details = models.TextField(
        blank=True,
        help_text="Please provide more details about your background"
    )
    
    tried_online_teaching = models.BooleanField(
        help_text="Have you considered or tried teaching online?"
    )
    online_teaching_reason = models.TextField(
        blank=True,
        help_text="Why or why not?"
    )
    
    teaching_challenges = models.TextField(
        help_text="What challenges do you face when teaching students now?"
    )
    
    students_per_week = models.IntegerField(
        validators=[MinValueValidator(0)],
        help_text="How many students could you realistically teach each week?"
    )
    
    preferred_session_length = models.IntegerField(
        choices=SESSION_LENGTH_CHOICES,
        help_text="What session length do you prefer to teach?"
    )
    
    fair_rate_etb = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text="What rate per session (in ETB) seems fair for you?"
    )
    
    confident_topics = models.JSONField(
        help_text="Which Islamic topics do you feel confident teaching?"
    )
    
    # Q8: Interest in platform
    would_join_platform = models.BooleanField(
        help_text="Would you join a platform that handles scheduling and student matching?"
    )
    
    # Q9: Support needed for effective teaching
    support_needed = models.TextField(
        help_text="What kind of support would you need to teach effectively online?"
    )
    
    # Q10: Concerns about online platform
    platform_concerns = models.TextField(
        blank=True,
        help_text="What concerns do you have about using an online teaching platform?"
    )
    
    # Q11: Student feedback collection
    feedback_preferences = models.TextField(
        help_text="How do you think students' feedback should be collected and shown?"
    )
    
    # Q12: Interest in early access
    wants_early_access = models.BooleanField(
        default=False,
        help_text="Would you be interested in early access?"
    )
    early_access_contact = models.CharField(
        max_length=255,
        blank=True,
        help_text="Contact info for early access (if different from phone)"
    )

    # Dynamic responses
    dynamic_responses = models.JSONField(
        default=dict,
        blank=True,
        help_text="Responses to dynamic questions based on confident topics"
    )

    submitted_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"Teacher Survey - {self.submitted_at.strftime('%Y-%m-%d %H:%M')}"

class SurveyQuestion(models.Model):
    SURVEY_TYPE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    ]
    
    QUESTION_TYPE_CHOICES = [
        ('choice', 'Multiple Choice'),
        ('text', 'Text Input'),
    ]

    survey_type = models.CharField(max_length=10, choices=SURVEY_TYPE_CHOICES)
    section = models.CharField(max_length=50) # e.g., 'Quran Reading'
    identifier = models.CharField(max_length=50) # e.g., 'quran_goal'
    
    # Text content (English & Arabic)
    text_en = models.TextField()
    text_ar = models.TextField()
    
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPE_CHOICES, default='choice')
    
    # Options (stored as JSON)
    options_en = models.JSONField(default=list, blank=True)
    options_ar = models.JSONField(default=list, blank=True)
    
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        unique_together = ['survey_type', 'identifier']

    def __str__(self):
        return f"{self.survey_type} - {self.identifier}"
