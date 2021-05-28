from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.http import JsonResponse

# Create your views here.

def index(request):
    latest_questions_list = Question.objects.order_by('pub_date')[:5]
    response = []
    for q in latest_questions_list:
        response.append(q.question_text)
    return JsonResponse(response, safe=False)

def detail(request,question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request,question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


