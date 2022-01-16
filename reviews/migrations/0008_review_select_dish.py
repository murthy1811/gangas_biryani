# Generated by Django 3.2.9 on 2022-01-15 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0002_auto_20220102_1230'),
        ('reviews', '0007_auto_20220115_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='select_dish',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='dishes.dish'),
        ),
    ]
