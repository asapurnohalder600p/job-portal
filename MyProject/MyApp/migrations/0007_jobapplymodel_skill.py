# Generated by Django 5.0.6 on 2024-10-27 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0006_jobapplymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplymodel',
            name='Skill',
            field=models.CharField(max_length=200, null=True),
        ),
    ]