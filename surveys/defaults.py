
DEFAULT_STUDENT_QUESTIONS = {
    'Quran Reading': [
        {
            'identifier': 'quran_goal',
            'text_en': 'What is your primary goal for learning Quran?',
            'text_ar': 'ما هو هدفك الأساسي من تعلم القرآن؟',
            'question_type': 'choice',
            'options_en': ['Reading with Tajweed', 'Memorization', 'Understanding meaning'],
            'options_ar': ['القراءة بالتجويد', 'الحفظ', 'فهم المعاني'],
            'order': 1
        },
    ],
    'Tajweed': [
        {
            'identifier': 'tajweed_level',
            'text_en': 'What is your current Tajweed level?',
            'text_ar': 'ما هو مستواك الحالي في التجويد؟',
            'question_type': 'choice',
            'options_en': ['Beginner', 'Intermediate', 'Advanced'],
            'options_ar': ['مبتدئ', 'متوسط', 'متقدم'],
            'order': 1
        },
        {
            'identifier': 'tajweed_knowledge',
            'text_en': 'Which Tajweed rules are you familiar with?',
            'text_ar': 'ما هي أحكام التجويد التي تعرفها؟',
            'question_type': 'choice',
            'options_en': ['Basic Nun Sakinah', 'Mudd Rules', 'Makharij (Exit Points)'],
            'options_ar': ['أحكام النون الساكنة', 'أحكام المد', 'مخارج الحروف'],
            'order': 2
        },
        {
            'identifier': 'tajweed_practice',
            'text_en': 'How often do you practice Tajweed?',
            'text_ar': 'كم مرة تمارس التجويد؟',
            'question_type': 'choice',
            'options_en': ['Daily', 'Weekly', 'Rarely'],
            'options_ar': ['يومياً', 'أسبوعياً', 'نادراً'],
            'order': 3
        }
    ],
    'Hadith': [
        {
            'identifier': 'hadith_collection',
            'text_en': 'Which Hadith collection are you interested in?',
            'text_ar': 'أي مجموعة حديث تهتم بها؟',
            'question_type': 'choice',
            'options_en': ['Sahih Bukhari', 'Sahih Muslim', '40 Hadith Nawawi', 'Riyad as-Salihin'],
            'options_ar': ['صحيح البخاري', 'صحيح مسلم', 'الأربعين النووية', 'رياض الصالحين'],
            'order': 1
        },
        {
            'identifier': 'hadith_focus',
            'text_en': 'What is your focus in Hadith studies?',
            'text_ar': 'ما هو تركيزك في دراسة الحديث؟',
            'question_type': 'choice',
            'options_en': ['General Understanding', 'Isnad (Chain of Narrators)', 'Fiqh of Hadith'],
            'options_ar': ['الفهم العام', 'الإسناد', 'فقه الحديث'],
            'order': 2
        },
        {
            'identifier': 'hadith_language',
            'text_en': 'Preferred language for Hadith explanation?',
            'text_ar': 'اللغة المفضلة لشرح الحديث؟',
            'question_type': 'choice',
            'options_en': ['English', 'Arabic', 'Amharic', 'Oromo'],
            'options_ar': ['الإنجليزية', 'العربية', 'الأمهرية', 'الأورومو'],
            'order': 3
        }
    ],
    'Arabic Language': [
        {
            'identifier': 'arabic_level',
            'text_en': 'Current Arabic proficiency?',
            'text_ar': 'مستوى إجادة اللغة العربية الحالي؟',
            'question_type': 'choice',
            'options_en': ['Beginner', 'Intermediate', 'Advanced'],
            'options_ar': ['مبتدئ', 'متوسط', 'متقدم'],
            'order': 1
        },
        {
            'identifier': 'arabic_goal',
            'text_en': 'Goal for learning Arabic?',
            'text_ar': 'الهدف من تعلم العربية؟',
            'question_type': 'choice',
            'options_en': ['Understanding Quran', 'Speaking/Conversation', 'Academic/Grammar', 'Business'],
            'options_ar': ['فهم القرآن', 'المحادثة', 'الدراسة/النحو', 'العمل'],
            'order': 2
        },
        {
            'identifier': 'arabic_dialect',
            'text_en': 'Preferred dialect?',
            'text_ar': 'اللهجة المفضلة؟',
            'question_type': 'choice',
            'options_en': ['Fusha (Modern Standard)', 'Egyptian', 'Levantine', 'Gulf', 'North African'],
            'options_ar': ['الفصحى', 'المصرية', 'الشامية', 'الخليجية', 'المغاربية'],
            'order': 3
        },
        {
            'identifier': 'arabic_schedule',
            'text_en': 'Preferred schedule intensity?',
            'text_ar': 'كثافة الجدول المفضلة؟',
            'question_type': 'choice',
            'options_en': ['Intensive (Daily)', 'Regular (2-3 times/week)', 'Casual (Weekend)'],
            'options_ar': ['مكثف (يومي)', 'منتظم (2-3 مرات/أسبوع)', 'عادي (نهاية الأسبوع)'],
            'order': 4
        }
    ],
    'Islamic Arts': [
        {
            'identifier': 'art_type',
            'text_en': 'Type of Islamic Art?',
            'text_ar': 'نوع الفن الإسلامي؟',
            'question_type': 'choice',
            'options_en': ['Calligraphy', 'Geometric Patterns', 'Illumination', 'Architecture History'],
            'options_ar': ['الخط العربي', 'الزخارف الهندسية', 'التذهيب', 'تاريخ العمارة'],
            'order': 1
        },
        {
            'identifier': 'art_level',
            'text_en': 'Experience level?',
            'text_ar': 'مستوى الخبرة؟',
            'question_type': 'choice',
            'options_en': ['Beginner', 'Hobbyist', 'Professional'],
            'options_ar': ['مبتدئ', 'هاوي', 'محترف'],
            'order': 2
        },
        {
            'identifier': 'art_goal',
            'text_en': 'Goal?',
            'text_ar': 'الهدف؟',
            'question_type': 'choice',
            'options_en': ['Personal Enjoyment', 'Professional Skill', 'Teaching'],
            'options_ar': ['متعة شخصية', 'مهارة مهنية', 'التعليم'],
            'order': 3
        }
    ]
}

DEFAULT_TEACHER_QUESTIONS = {
    'Quran Reading': [
        {
            'identifier': 'quran_teaching_exp',
            'text_en': 'Level you are qualified to teach?',
            'text_ar': 'المستوى الذي أنت مؤهل لتدريسه؟',
            'question_type': 'choice',
            'options_en': ['Beginner', 'Intermediate', 'Advanced'],
            'options_ar': ['مبتدئ', 'متوسط', 'متقدم'],
            'order': 1
        },
    ],
    'Tajweed': [
        {
            'identifier': 'tajweed_level',
            'text_en': 'Level you are qualified to teach?',
            'text_ar': 'المستوى الذي أنت مؤهل لتدريسه؟',
            'question_type': 'choice',
            'options_en': ['Beginner', 'Intermediate', 'Advanced'],
            'options_ar': ['مبتدئ', 'متوسط', 'متقدم'],
            'order': 1
        },
        {
            'identifier': 'tajweed_knowledge',
            'text_en': 'Tajweed rules you can teach?',
            'text_ar': 'أحكام التجويد التي يمكنك تدريسها؟',
            'question_type': 'choice',
            'options_en': ['Basic Nun Sakinah', 'Mudd Rules', 'Makharij (Exit Points)'],
            'options_ar': ['أحكام النون الساكنة', 'أحكام المد', 'مخارج الحروف'],
            'order': 2
        }
    ],
    'Hadith': [
        {
            'identifier': 'hadith_collection',
            'text_en': 'Collections you can teach?',
            'text_ar': 'المجموعات التي يمكنك تدريسها؟',
            'question_type': 'choice',
            'options_en': ['Sahih Bukhari', 'Sahih Muslim', '40 Hadith Nawawi', 'Riyad as-Salihin'],
            'options_ar': ['صحيح البخاري', 'صحيح مسلم', 'الأربعين النووية', 'رياض الصالحين'],
            'order': 1
        },
        {
            'identifier': 'hadith_language',
            'text_en': 'Languages you can teach in?',
            'text_ar': 'اللغات التي يمكنك التدريس بها؟',
            'question_type': 'choice',
            'options_en': ['English', 'Arabic', 'Amharic', 'Oromo'],
            'options_ar': ['الإنجليزية', 'العربية', 'الأمهرية', 'الأورومو'],
            'order': 2
        }
    ],
    'Arabic Language': [
        {
            'identifier': 'arabic_teaching_level',
            'text_en': 'Level you can teach?',
            'text_ar': 'المستوى الذي يمكنك تدريسه؟',
            'question_type': 'choice',
            'options_en': ['Beginner', 'Intermediate', 'Advanced'],
            'options_ar': ['مبتدئ', 'متوسط', 'متقدم'],
            'order': 1
        },
        {
            'identifier': 'arabic_dialect',
            'text_en': 'Dialects you can teach?',
            'text_ar': 'اللهجات التي يمكنك تدريسها؟',
            'question_type': 'choice',
            'options_en': ['Fusha (Modern Standard)', 'Egyptian', 'Levantine', 'Gulf', 'North African'],
            'options_ar': ['الفصحى', 'المصرية', 'الشامية', 'الخليجية', 'المغاربية'],
            'order': 2
        }
    ],
    'Islamic Arts': [
        {
            'identifier': 'art_type',
            'text_en': 'Arts you can teach?',
            'text_ar': 'الفنون التي يمكنك تدريسها؟',
            'question_type': 'choice',
            'options_en': ['Calligraphy', 'Geometric Patterns', 'Illumination', 'Architecture History'],
            'options_ar': ['الخط العربي', 'الزخارف الهندسية', 'التذهيب', 'تاريخ العمارة'],
            'order': 1
        },
        {
            'identifier': 'art_level',
            'text_en': 'Level you can teach?',
            'text_ar': 'المستوى الذي يمكنك تدريسه؟',
            'question_type': 'choice',
            'options_en': ['Beginner', 'Hobbyist', 'Professional'],
            'options_ar': ['مبتدئ', 'هاوي', 'محترف'],
            'order': 2
        }
    ]
}
