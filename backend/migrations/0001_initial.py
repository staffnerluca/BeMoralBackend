# Generated by Django 5.0.7 on 2024-07-14 15:17

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('goal', models.TextField()),
                ('moral_type', models.CharField(max_length=20)),
                ('course_type', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='CourseQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('goal', models.TextField()),
                ('relevant_for', models.CharField(max_length=20)),
                ('interactive', models.BooleanField()),
                ('multiple_choice_quiz', models.BooleanField()),
                ('info_screen', models.BooleanField()),
                ('image', models.ImageField(upload_to='')),
                ('furhter_resources', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DoingGoodNetworkPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('post_date', models.DateField()),
                ('commentsOn', models.IntegerField()),
                ('violates_conde_of_conduct', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='GoodThing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('impact', models.CharField(max_length=200)),
                ('creator', models.CharField(max_length=20)),
                ('relevant_for', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('second_name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=2)),
                ('age', models.IntegerField()),
                ('isAdmin', models.BooleanField()),
                ('categorical_imperative', models.IntegerField()),
                ('utilitarian', models.IntegerField()),
                ('virtue_ethics', models.IntegerField()),
                ('animal_rights', models.IntegerField()),
                ('longtermism', models.IntegerField()),
                ('wants_to_become_vegetarian', models.BooleanField()),
                ('doing_good_streak', models.IntegerField()),
                ('not_eating_meat_streak', models.IntegerField()),
                ('course_streak', models.IntegerField()),
                ('joined_at', models.DateField(default=django.utils.timezone.now)),
                ('total_time_on_the_app_in_minutes', models.BigIntegerField()),
                ('total_amount_of_donations', models.IntegerField()),
                ('donations_per_week_goal', models.IntegerField()),
                ('meat_days', models.CharField(max_length=12)),
                ('goodness_score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email_address', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='LikedPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.doinggoodnetworkpost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='DoneQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.coursequestion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='DoneGoodThings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good_thing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.goodthing')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='DoneCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coures', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='doinggoodnetworkpost',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.userprofile'),
        ),
        migrations.AddField(
            model_name='coursequestion',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.userprofile'),
        ),
        migrations.AddField(
            model_name='course',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.userprofile'),
        ),
    ]
