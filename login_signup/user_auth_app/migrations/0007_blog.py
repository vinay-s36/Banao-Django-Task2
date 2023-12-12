# Generated by Django 4.1.7 on 2023-12-11 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth_app', '0006_alter_userprofile_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('summary', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image_url', models.URLField()),
                ('is_draft', models.BooleanField(default=False)),
                ('category', models.CharField(choices=[('Mental Health', 'Mental Health'), ('Heart Disease', 'Heart Disease'), ('Covid19', 'Covid19'), ('Immunization', 'Immunization')], max_length=50)),
                ('author', models.ForeignKey(limit_choices_to={'user_type': 'doctor'}, on_delete=django.db.models.deletion.CASCADE, to='user_auth_app.userprofile')),
            ],
        ),
    ]