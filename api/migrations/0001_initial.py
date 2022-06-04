# Generated by Django 4.0.1 on 2022-06-04 19:48

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('meta', models.JSONField(default=dict)),
                ('is_active', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updated_%(class)ss', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'campaigns',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField()),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.campaign')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updated_%(class)ss', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'surveys',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='UserResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('interview_uuid', models.CharField(max_length=25, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=14)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.survey')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updated_%(class)ss', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_responses',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='SurveyCollector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.survey')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updated_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'survey_collectors',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question', models.TextField()),
                ('type', models.CharField(choices=[('text', 'text'), ('short_text', 'short_text'), ('radio', 'radio'), ('select', 'select'), ('select_image', 'select_image'), ('select_multiple', 'select_multiple'), ('email', 'email'), ('integer', 'integer'), ('float', 'float'), ('link', 'link'), ('date', 'Date')], max_length=100)),
                ('choices', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, null=True, size=None)),
                ('is_required', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.survey')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updated_%(class)ss', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'questions',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(blank=True, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.question')),
                ('user_response', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.userresponse')),
            ],
            options={
                'db_table': 'answers',
            },
        ),
        migrations.AddIndex(
            model_name='userresponse',
            index=models.Index(fields=['-created_at'], name='user_respon_created_270cf0_idx'),
        ),
        migrations.AddIndex(
            model_name='survey',
            index=models.Index(fields=['-created_at'], name='surveys_created_cd56de_idx'),
        ),
        migrations.AddIndex(
            model_name='survey',
            index=models.Index(fields=['is_active'], name='surveys_is_acti_55133e_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='survey',
            unique_together={('campaign', 'name')},
        ),
        migrations.AddIndex(
            model_name='question',
            index=models.Index(fields=['-created_at'], name='questions_created_fc8d7e_idx'),
        ),
        migrations.AddIndex(
            model_name='question',
            index=models.Index(fields=['is_active'], name='questions_is_acti_ba6b3c_idx'),
        ),
        migrations.AddIndex(
            model_name='campaign',
            index=models.Index(fields=['-created_at'], name='campaigns_created_163163_idx'),
        ),
        migrations.AddIndex(
            model_name='campaign',
            index=models.Index(fields=['is_active'], name='campaigns_is_acti_6c57d0_idx'),
        ),
    ]
