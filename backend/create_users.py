from datetime import timedelta
from django.utils import timezone
from .models import CustomUser, UserProfile

for i in range(10):
    email = f"user{i}@ex.com"
    user = CustomUser.objects.create_user(email_address=email, password='password')

    UserProfile.objects.create(
        user=user,
        first_name=f"FirstName{i}",
        second_name=f"SecondName{i}",
        username=f"username{i}",
        country="US",
        brit_date=timezone.now().date() - timedelta(days=i * 365),
        isAdmin=bool(i % 2),
        wants_to_become_vegetarian=bool(i % 3),
        not_eating_meat_streak=i * 5,
        course_streak=i * 2,
        joined_at=timezone.now().date() - timedelta(days=i * 30),
        total_time_on_the_app_in_minutes=i * 100,
        meat_days="Mo,Fr" if i % 2 == 0 else "Tu,Th"
    )

print("10 example datasets created.")
