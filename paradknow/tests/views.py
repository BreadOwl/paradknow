from django.shortcuts import render, get_object_or_404, redirect
from .models import Topic, Question
from django import forms
import random

#форма для темы
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'topic', 'answer']

#список тем + добавление
def index(request):
    topics = Topic.objects.all()

    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TopicForm()

    return render(request, 'index.html', {
        'topics': topics,
        'form': form,
    })

#редактирование темы
def topic_edit(request, pk):
    topic = get_object_or_404(Topic, pk=pk)

    if request.method == 'POST':
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TopicForm(instance=topic)

    return render(request, 'topics/edit_topic.html', {
        'form': form,
        'topic': topic,
    })

#удаление темы
def topic_delete(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    topic.delete()
    return redirect('index')

#страница темы
def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    questions = topic.questions.all()  #получаем вопросы

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.topic = topic
            question.save()
            return redirect('topic_detail', pk=topic.pk)
    else:
        form = QuestionForm()

    return render(request, 'topics/shab_topic.html', {
        'topic': topic,
        'questions': questions,
        'form': form,
    })

def question_add(request, topic_pk):
    topic = get_object_or_404(Topic, pk=topic_pk)

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.topic = topic
            question.save()
            return redirect('topic_detail', pk=topic.pk)
    else:
        form = QuestionForm(initial={'topic': topic})

    return render(request, 'quests/create_quest.html', {
        'form': form,
        'topic': topic,
    })

def question_edit(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('topic_detail', pk=question.topic.pk)
    else:
        form = QuestionForm(instance=question)

    return render(request, 'quests/edit_quest.html', {
        'form': form,
        'question': question,
    })


def question_delete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    topic_pk = question.topic.pk
    question.delete()
    return redirect('topic_detail', pk=topic_pk)

def checkyoslf(request, topic_pk):
    # Получаем все вопросы по теме
    questions = list(Question.objects.filter(topic_id=topic_pk))
    
    if questions:
        question = random.choice(questions)
    else:
        question = None

    return render(request, 'checkyoslf.html', {
        'question': question,
        'topic_pk': topic_pk,
    })

