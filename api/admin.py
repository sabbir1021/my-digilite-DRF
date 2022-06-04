from django.contrib import admin
from .models import Campaign , Survey , Question, UserResponse , Answer , SurveyCollector
# # Register your models here.


admin.site.register(Campaign)
admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UserResponse)
admin.site.register(SurveyCollector)