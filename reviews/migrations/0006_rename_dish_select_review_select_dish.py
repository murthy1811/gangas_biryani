# Generated by Django 3.2.9 on 2022-01-15 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_review_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='dish_select',
            new_name='select_dish',
        ),
    ]
