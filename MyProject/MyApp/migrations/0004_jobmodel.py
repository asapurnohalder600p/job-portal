# Generated by Django 5.0.6 on 2024-10-27 04:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_alter_custom_user_model_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100, null=True)),
                ('Openings', models.CharField(max_length=100, null=True)),
                ('Category', models.CharField(choices=[('full_time', 'Full Time'), ('part_time', 'Part Time')], max_length=100, null=True)),
                ('Job_Dscriptions', models.TextField(null=True)),
                ('Skill', models.CharField(choices=[('python', 'PYTHON'), ('java', 'JAVA'), ('graphic', 'GRAPHIC'), ('marketing', 'MERKETING')], max_length=100, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
