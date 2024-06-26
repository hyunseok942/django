from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Question
from django.utils import timezone
from  .forms import Question
from  django.http import HttpResponse
def index(request):
    #question_list=Question.objects.all()
    #order_by('속성명'), order_by('-속성명')
    question_list = Question.objects.order_by('create_date')
    context={'question_list':question_list}
    return  render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    context={'question':question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:details', question_id=question.id)

def greet(request):
    return  HttpResponse("반갑습니다")

def question_create(request):
    form=QuestionForm()
    return render(request, 'pybo/question_form.html', {'form':form})