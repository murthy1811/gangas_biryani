# Generated by Django 3.2.9 on 2022-01-15 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0010_alter_review_select_dish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='select_dish',
        ),
    ]
