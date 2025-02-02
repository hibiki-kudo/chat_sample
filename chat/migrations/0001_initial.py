# Generated by Django 3.0.5 on 2020-04-04 08:57

import uuid

import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import chat.models.user


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('username',
                 models.CharField(blank=True, error_messages={'unique': 'A user with that username already exists.'},
                                  help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                                  max_length=150, verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('level', models.FloatField(default=1, verbose_name='レベル')),
                ('user_id', models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='ユーザID')),
                ('is_login', models.BooleanField(default=False, verbose_name='ログイン中')),
                ('is_staff', models.BooleanField(default=False,
                                                 help_text='Designates whether the user can log into this admin site.',
                                                 verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True,
                                                  help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
                                                  verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_to', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', chat.models.user.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'チャットルーム',
                'verbose_name_plural': 'チャットルーム',
                'db_table': 'room',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('abstractuser_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='chat.AbstractUser')),
            ],
            options={
                'abstract': False,
                'swappable': 'AUT_USER_MODEL',
            },
            bases=('chat.abstractuser',),
            managers=[
                ('objects', chat.models.user.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('message', models.TextField(max_length=500)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.Room')),
                ('user', models.ForeignKey(on_delete=models.SET(0), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'メッセージ',
                'verbose_name_plural': 'メッセージ',
                'db_table': 'message',
            },
        ),
    ]
