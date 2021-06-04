import random
import json

from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.http import JsonResponse
from django.utils import timezone
from .tenant_manage import create_schema,connect_to_schema

# Create your views here.

def index(request):
    return JsonResponse({"error" : "Provide the valid tenant id in the url -> polls/{tenantId}"})

def detail(request,question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def tenant_index(request,tenant_id):
    try:
        connect_to_schema(tenant_id)
        latest_questions_list = Question.objects.order_by('pub_date')[:5]
        questions = []
        # send question text as response
        for q in latest_questions_list:
            key_value = {}
            key_value['question'] = q.question_text
            key_value['date'] = q.pub_date
            questions.append(key_value)

        response_object = {
            "tenant_info" : 
                {
                "schema": tenant_id
                },
            "questions" : questions
            }
        return JsonResponse(response_object,safe=False)
    except Exception as ex:
        print(ex)
        return JsonResponse({
            "error" : "Invalid tenant"
        })


def results(request,question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def insert_for_tenant(request,tenant_id):
    try:
        connect_to_schema(tenant_id)
        text = "Bazinga " + str(random.randrange(100)) + " ?"
        question = Question(question_text = text, pub_date=timezone.now())
        question.save()
        return JsonResponse(question.question_text, safe=False)
    except Exception:
        return JsonResponse({"error" : "Invalid tenant"})

def onboard(request):
    schema = create_schema()
    response = {
        "created" : schema,
        "url" : "http://localhost:8000/polls/" + schema
    }
    return JsonResponse(response)


