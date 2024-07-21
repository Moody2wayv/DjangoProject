from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UserRegistrationForm  # importing the registration form
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Choice, Question
from django.contrib.auth.models import User

def user_login(request):
    return render(request, 'authentication/login.html')


def authenticate_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponseRedirect(reverse('user_auth:login'))
        else:
            login(request, user)
            return HttpResponseRedirect(reverse('polls:index'))  # Redirecting to polls app


def show_user(request):
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'authentication/register_done.html', {'new_user': new_user})
    else:
        form = UserRegistrationForm()
    return render(request, 'authentication/register.html', {'form': form}) 


# Restricting voting to users logged-in .
@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
