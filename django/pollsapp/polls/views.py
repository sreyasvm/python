import random

from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.http import JsonResponse
from django.utils import timezone
from .tenant_manage import create_schema,connect_to_schema

# Create your views here.

TENANT_SCHEMA = "tenant67"

def index(request):
    connect_to_schema(TENANT_SCHEMA)
    latest_questions_list = Question.objects.order_by('pub_date')[:5]
    response = []
    # send question text as response
    for q in latest_questions_list:
        key_value = {}
        key_value['question'] = q.question_text
        key_value['date'] = q.pub_date
        response.append(key_value)
    return JsonResponse(response, safe=False)

def detail(request,question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request,question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def insert(request):
    connect_to_schema(TENANT_SCHEMA)
    text = "Bazinga " + str(random.randrange(100)) + " ?"
    question = Question(question_text = text, pub_date=timezone.now())
    question.save()
    return JsonResponse(question.question_text, safe=False)

def create(request):
    schema = create_schema()
    response = {"created" : schema}
    return JsonResponse(response)


