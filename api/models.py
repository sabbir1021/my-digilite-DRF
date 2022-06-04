from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth import get_user_model
User = get_user_model()

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='created_%(class)ss')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='updated_%(class)ss', null=True, blank=True)

    class Meta:
        abstract = True


class AnswerTypeChoices(models.TextChoices):
    TEXT = 'text', 'text'
    SHORT_TEXT = 'short_text', 'short_text'
    RADIO = 'radio', 'radio'
    SELECT = 'select', 'select'
    SELECT_IMAGE = 'select_image', 'select_image'
    SELECT_MULTIPLE = 'select_multiple', 'select_multiple'
    EMAIL = 'email', 'email'
    INTEGER = 'integer', 'integer'
    FLOAT = 'float', 'float'
    LINK = 'link', 'link'
    DATE = "date"

class Campaign(BaseModel):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    meta = models.JSONField(default=dict)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        db_table = 'campaigns'
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['is_active'])
        ]
    
    def __str__(self):
        return str(self.name)
    
class Survey(BaseModel):
    campaign = models.ForeignKey('api.Campaign', on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField()

    class Meta:
        ordering = ['-created_at']
        db_table = 'surveys'
        unique_together = ('campaign', 'name')
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['is_active'])
        ]
    
    def __str__(self):
        return str(self.name)

class Question(BaseModel):
    survey = models.ForeignKey('api.Survey', on_delete=models.PROTECT)
    question = models.TextField()
    type = models.CharField(max_length = 100, choices=AnswerTypeChoices.choices)
    choices = ArrayField(models.CharField(max_length=100), blank=True, null = True)
    is_required = models.BooleanField()
    is_active = models.BooleanField()

    class Meta:
        ordering = ['-created_at']
        db_table = 'questions'
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['is_active'])
        ]
    
    def __str__(self):
        return str(self.question)


class UserResponse(BaseModel):
    survey = models.ForeignKey('api.Survey', on_delete=models.PROTECT)
    interview_uuid = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)

    class Meta:
        ordering = ['-created_at']
        db_table = 'user_responses'
        indexes = [
            models.Index(fields=['-created_at']),
        ]
    
    def __str__(self):
        return str(self.interview_uuid)


class Answer(models.Model):
    user_response = models.ForeignKey('api.UserResponse', on_delete=models.PROTECT)
    question = models.ForeignKey('api.Question', on_delete=models.PROTECT)
    answer = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'answers'
    
    def __str__(self):
        return str(self.answer)


class SurveyCollector(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    survey = models.ForeignKey('api.Survey', on_delete=models.PROTECT)

    class Meta:
        db_table = 'survey_collectors'
