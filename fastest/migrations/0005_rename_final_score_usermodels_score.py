# Generated by Django 4.0.6 on 2022-08-09 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fastest', '0004_alter_usermodels_passed_tests'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodels',
            old_name='final_score',
            new_name='score',
        ),
    ]
