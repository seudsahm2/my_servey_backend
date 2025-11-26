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
    
    full_name = models.CharField(
        max_length=255,
        blank=False,
        default='',
        help_text="Full name of the student"
    )

    # Q0: Phone Number (Identity)
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        blank=True,
        help_text="Phone number for identity verification (e.g., +251...)"
    )

    # Q1: Current experience reading the Quran
    quran_experience = models.CharField(
        max_length=20,
        choices=EXPERIENCE_CHOICES,
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
    
    # Q0: Phone Number (Identity)
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        help_text="Phone number for identity verification (e.g., +251...)"
    )

    # Q1: Teaching background
    teaching_background = models.CharField(
        max_length=20,
        choices=TEACHING_BACKGROUND_CHOICES,
        help_text="What is your teaching background?"
    )
    teaching_background_details = models.TextField(
        blank=True,
        help_text="Please provide more details about your background"
    )
    
    # Q2: Considered or tried teaching online
    tried_online_teaching = models.BooleanField(
        help_text="Have you considered or tried teaching online?"
    )
    online_teaching_reason = models.TextField(
        blank=True,
        help_text="Why or why not?"
    )
    
    # Q3: Current teaching challenges
    teaching_challenges = models.TextField(
        help_text="What challenges do you face when teaching students now?"
    )
    
    # Q4: Number of students per week
    students_per_week = models.IntegerField(
        validators=[MinValueValidator(0)],
        help_text="How many students could you realistically teach each week?"
    )
    
    # Q5: Preferred session length
    preferred_session_length = models.IntegerField(
        choices=SESSION_LENGTH_CHOICES,
        help_text="What session length do you prefer to teach?"
    )
    
    # Q6: Fair rate per session in ETB
    fair_rate_etb = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text="What rate per session (in ETB) seems fair for you?"
    )
    
    # Q7: Topics confident teaching (stored as JSON array)
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

    submitted_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"Teacher Survey - {self.submitted_at.strftime('%Y-%m-%d %H:%M')}"
