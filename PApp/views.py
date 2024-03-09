from django.shortcuts import render, redirect
from .models import Project
from .models import Skill
from .models import Achievement
from django.http import HttpResponse


def about(request):
    return render(request , 'about.html')


def send_email(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('body')

        recipient_email = "charantej6ms@gmail.com"
        gmail_url = f"https://mail.google.com/mail/u/0/?view=cm&fs=1&to={recipient_email}&su={subject}&body={message}"

        return redirect(gmail_url)
    elif request.method == 'GET':
        return render(request, 'mail.html')
    else:
        return HttpResponse("Unsupported request method.")


def achievements(request):
    achievements = Achievement.objects.all()
    context = {'achievements': achievements}
    return render(request, 'achievements.html', context)


def skills(request):
    skills = Skill.objects.all()
    context = {'skills': skills}
    return render(request, 'skills.html', context)


def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})


def index(request):
    return render(request, 'home.html')
