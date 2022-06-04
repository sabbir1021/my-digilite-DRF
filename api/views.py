from rest_framework.response import Response
from .models import Campaign , Survey , Question, UserResponse , Answer , SurveyCollector
from .serializers import CampaignSerlializer,SurveySerializer, QuestionSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import Http404 
from django.db import transaction

# Create your views here.


class CampaignList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        campaign = Campaign.objects.all()
        serializer = CampaignSerlializer(campaign, many=True)
        response = {
            "Status": True,
            "Message": "Seccessful",
            "Count" : campaign.count(),
            "Data" : serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, format=None): 
        request.data["created_by"] = request.user.id
        serializer = CampaignSerlializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            response = {
            "Status": True,
            "Message": "Created",
            "Data" : serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            "Status": False,
            "Message": "Bad Request",
            "Data" : serializer.errors
            }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    
class CampaignListSingle(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Campaign.objects.get(pk=pk)
        except Campaign.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        campaign = self.get_object(pk)
        serializer = CampaignSerlializer(campaign)
        response = {
            "Status": True,
            "Message": "Seccessful",
            "Data" : serializer.data
        }
        return Response(response)

    def patch(self, request, pk, format=None):
        campaign = self.get_object(pk)
        request.data["updated_by"] = request.user.id
        serializer = CampaignSerlializer(campaign, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SurveyList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        survey = Survey.objects.all()
        serializer = SurveySerializer(survey, many=True)
        response = {
            "Status": True,
            "Message": "Seccessful",
            "Count" : survey.count(),
            "Data" : serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, format=None): 
        request.data["created_by"] = request.user.id
        serializer = SurveySerializer(data=request.data) 
        if serializer.is_valid():
            survey = serializer.save()
            all_data = []
            for question in request.data["question_set"]:
                question['survey'] = survey.id
                question['created_by'] = request.user.id
                all_data.append(question)
            serializer_question = QuestionSerializer(data=all_data, many = True)
            if serializer_question.is_valid():
                serializer_question.save()
            response = {
            "Status": True,
            "Message": "Created",
            "Data" : serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        
        response = {
            "Status": False,
            "Message": "Bad Request",
            "Data" : serializer.errors
            }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)