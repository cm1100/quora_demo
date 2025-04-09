from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.contrib.auth.decorators import login_required

@login_required
def post_question(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        question = form.save(commit=False)
        question.author = request.user
        question.save()
        return redirect('home')
    return render(request, 'post_question.html', {'form': form})

@login_required
def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = question.answers.all()
    answer_form = AnswerForm(request.POST or None)
    if answer_form.is_valid():
        answer = answer_form.save(commit=False)
        answer.author = request.user
        answer.question = question
        answer.save()
        return redirect('question_detail', question_id=question_id)
    return render(request, 'question_detail.html', {'question': question, 'answers': answers, 'form': answer_form})

@login_required
def like_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    if request.user not in answer.likes.all():
        answer.likes.add(request.user)
    return redirect('question_detail', question_id=answer.question.id)


def home(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'questions': questions})