# Generated by Django 5.0.6 on 2024-07-17 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Graduation_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
