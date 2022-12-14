# Generated by Django 4.0.6 on 2022-08-10 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_quiztaker_completed_alter_answer_question_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiztaker',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.question'),
        ),
        migrations.AlterField(
            model_name='quiztaker',
            name='data_finished',
            field=models.IntegerField(null=True),
        ),
    ]
