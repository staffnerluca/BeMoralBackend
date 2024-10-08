from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    get_current_course_lesson,
    get_eating_meat_days,
    login_view,
    register,
    create_test_users,
    get_all_users,
    create_test_days,
    get_calendar,
    get_data_for_vegetarian_streak_page,
    create_user_profile,
    get_calendar_test,
    get_all_days,
    get_questions_by_course,
    create_example_course_questions,
    get_course,
    get_all_courses,
    is_free_day,
    post_did_user_eat_meat,
    get_username_from_mail,
    moarality_chatbot,
    get_current_streak
)

urlpatterns = [
    path('get_current_course_lesson/', get_current_course_lesson, name='get_current_course_lesson'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('get_meat_days/', get_eating_meat_days, name='get_meat_days'),
    path('create_test_users/', create_test_users, name='create_test_users'),
    path('get_all_users/', get_all_users, name='get_all_users'),
    path('create_test_days/', create_test_days, name='create_test_days'),
    path('get_calendar/', get_calendar, name='get_calendar'),
    path('get_data_for_vegetarian_streak_page/<str:username>/', get_data_for_vegetarian_streak_page, name='get_data_for_vegetarian_streak_page'),
    path('create_user_profile/', create_user_profile, name='create_user_profile'),
    path('get_calendar_test/', get_calendar_test, name='get_calendar_test'),
    path('course-questions/<int:course_id>/', get_questions_by_course, name='get_questions_by_course'),
    path('get_all_days/', get_all_days, name='get_all_days'),
    path('create_example_course/', create_example_course_questions, name='create_example_course_questions'),
    path('get_course/<int:course_id>/', get_course, name='get_course'),
    path('get_all_courses/', get_all_courses, name='get_all_courses'),
    path('is_free_day/', is_free_day, name='is_free_day'),
    path('post_did_user_eat_meat', post_did_user_eat_meat, name='post_did_user_eat_meat'),
    path('get_username_from_mail/', get_username_from_mail, name='get_username_from_mail'),
    path('morality_chatbot', moarality_chatbot, name='morality_chatbot'),
    path('get_current_streak/<str:username>', get_current_streak, name='get_current_streak')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
