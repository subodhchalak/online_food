# Generated by Django 4.1.1 on 2022-10-15 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Username')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('phone_number', models.CharField(blank=True, max_length=12, verbose_name='Phone Number')),
                ('role', models.CharField(blank=True, choices=[('REASTAURANT', 'Restaurant'), ('CUSTOMER', 'Customer')], max_length=20, null=True, verbose_name='Role')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date Joined')),
                ('last_login', models.DateTimeField(auto_now_add=True, verbose_name='Last Login')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Is Admin')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Is Staff')),
                ('is_superadmin', models.BooleanField(default=False, verbose_name='Is Superadmin')),
                ('is_active', models.BooleanField(default=True, verbose_name='is Active')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]