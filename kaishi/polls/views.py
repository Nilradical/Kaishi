from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Question, Choice

def index(req):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #output = ', '.join([q.question_text for q in latest_question_list])
    context = {
        'latest_question_list': latest_question_list,
    }
    #return HttpResponse(template.render(context, req))
    return render(req, 'polls/index.html', context)

def detail(req, question_id):
    #question = Question.objects.get(pk=question_id)
    question = get_object_or_404(Question, pk= question_id)
    #raise Http404("Question does not exist")
    #return HttpResponse("You're looking at question %s." % question_id)
    return render(req, 'polls/detail.html', {'question': question})

def results(req, question_id):
    response = "You're looking at results of question %s."
    return HttpResponse(response % question_id)

def vote(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pl=req.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(req, 'polls.detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

def results(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(req, 'polls/results.html', {'question': question})

