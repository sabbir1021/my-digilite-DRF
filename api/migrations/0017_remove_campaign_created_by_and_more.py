# Generated by Django 4.0.5 on 2022-06-04 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_answer_campaign_question_survey_surveycollector_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='question',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='question',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='surveycollector',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='surveycollector',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='userresponse',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='userresponse',
            name='updated_by',
        ),
    ]
