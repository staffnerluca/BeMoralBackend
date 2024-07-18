from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):
    email_address = models.EmailField(unique=True, verbose_name="email")

    USERNAME_FIELD = 'email_address'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email_address


class UserProfile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    country = models.CharField(max_length=2) #only country code
    brit_date = models.DateField()
    isAdmin = models.BooleanField()

    #moral alignment in %
    categorical_imperative = models.IntegerField()
    utilitarian = models.IntegerField()
    virtue_ethics = models.IntegerField()
    animal_rights = models.IntegerField()
    longtermism = models.IntegerField()

    wants_to_become_vegetarian = models.BooleanField()
    doing_good_streak = models.IntegerField()
    not_eating_meat_streak = models.IntegerField()
    course_streak = models.IntegerField()
    joined_at = models.DateField(default=timezone.now)
    total_time_on_the_app_in_minutes = models.BigIntegerField()
    total_amount_of_donations = models.IntegerField()
    donations_per_week_goal = models.IntegerField()
    #the days a person wants to eat meat. For example if it is monday and friday MoFr
    meat_days = models.CharField(max_length=12)
    goodness_score = models.IntegerField()
    current_leaderboard_group = models.ForeignKey(models)


class DoingGoodStreaks():
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.DateField()


class EthicalTypes():
    name = models.CharField(max_length=100)
    #the et of an individual is determined as the et closest to their values
    categorical_imperative = models.IntegerField()
    utilitarian = models.IntegerField()
    virtue_ethics = models.IntegerField()
    animal_rights = models.IntegerField()
    longtermism = models.IntegerField()


class Course(models.Model):
    name = models.CharField(max_length=50)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE) #id of the creator
    goal = models.TextField()
    moral_type = models.CharField(max_length=20) # is there a school of thought that is presented in this course
    course_type = models.CharField(max_length=2)


class CourseQuestion(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    goal = models.TextField()
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    #defines for which moral groups this can be relevant
    relevant_for = models.CharField(max_length=20)
    interactive = models.BooleanField()
    #multiple choice quizes are stored with a special syntax in content
    multiple_choice_quiz = models.BooleanField()
    info_screen = models.BooleanField()
    image = models.CharField(max_length=1000)
    furhter_resources = models.TextField()


class GoodThing(models.Model):
    name = models.CharField(max_length=100)
    impact = models.CharField(max_length=200)
    creator = models.CharField(max_length=20)
    #defines for which moral groups this can be relevant
    relevant_for = models.ManyToManyField('EthicalTypes')
    thing_type = models.CharField(max_length=20) # for example donation, personal, voluntary opportunity...
    multiple_times = models.BooleanField()


class Issues(models.Model):
    issue_name = models.CharField(max_length=100)


class DoneGoodThings(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    good_thing = models.ForeignKey(GoodThing, on_delete=models.CASCADE)


class DoneQuestions(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course_question = models.ForeignKey(CourseQuestion, on_delete=models.CASCADE)


"""
could be determined by the done Course Questions but if they change a finished course would be shown to be unfinished
and it just saves server side calculation power to do it that way for a very moderate cost in memory
"""
class DoneCourses(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    coures = models.ForeignKey(Course, on_delete=models.CASCADE)


class DoingGoodNetworkPost(models.Model):
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.TextField()
    post_date = models.DateField()
    # is it a comment to an other post if yes to which?
    commentsOn = models.IntegerField()
    violates_conde_of_conduct = models.BooleanField()


class LikedPosts(models.Model):
    post = models.ForeignKey(DoingGoodNetworkPost, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
