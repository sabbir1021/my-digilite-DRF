from rest_framework import serializers
from .models import Campaign , Survey , Question, UserResponse , Answer , SurveyCollector
from django.contrib.auth.models import User
from rest_framework.serializers import SerializerMethodField

# class ReadWriteSerializerMethodField(SerializerMethodField):
#     def __init__(self, method_name=None, **kwargs):
#         self.method_name = method_name
#         kwargs["source"] = "*"
#         self.read_only = False
#         super(SerializerMethodField, self).__init__(**kwargs)

#     def to_internal_value(self, data):
#         return {f'{self.field_name}_id': data}

class UserLiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']

class SurveyLiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['id', 'name', 'is_active']

class CampaignSerlializer(serializers.ModelSerializer):
    created_by = UserLiteSerializer(read_only = True)
    survey_set =  SurveyLiteSerializer(many = True, read_only = True)
    # created_by = ReadWriteSerializerMethodField()
    # def get_created_by(self, obj):
    #     return UserLiteSerializer(obj.created_by, many=False).data
    
    class Meta:
        model = Campaign
        fields = ['id','name','description','start_date','end_date','meta', 'is_active','survey_set','created_by']
        extra_kwargs = {'created_by': {'write_only': True}, 'id':{'read_only':True}}


class QuestionLiteSerializer(serializers.ModelSerializer):
    created_by = UserLiteSerializer(read_only = True)
    class Meta:
        model = Question
        fields = ['id', 'question','type','choices','is_required','is_active','created_by']
        

class SurveySerializer(serializers.ModelSerializer):
    question_set =  QuestionLiteSerializer(many = True, read_only = True)
    class Meta:
        model = Survey
        fields = ['id', 'name','campaign','question_set', 'is_active','created_by']
        extra_kwargs = {'created_by': {'write_only': True}, 'id':{'read_only':True}}



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question','survey', 'type','choices','is_required','is_active','created_by']
        extra_kwargs = {'created_by': {'write_only': True}, 'id':{'read_only':True}}