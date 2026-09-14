from django.shortcuts import render

from main.models import Experience
from .models import Experience, Award, Skill


def show_main(request):
    context = {
        "name": "Nanda Athaillah Nurano",
        "npm": "2506557425",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "A Computer Science student at Universitas Indonesia interested "
            "in software development and education."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Nanda Athaillah Nurano",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_awards(request):
    awards = Award.objects.all()
    context = {
        "award_list": awards,
        "name": "Nanda Athaillah Nurano" 
    }
    return render(request, "awards.html", context)

def show_skills(request):
    skills = Skill.objects.all()
    context = {
        "skill_list": skills,
        "name": "Nanda Athaillah Nurano"
    }
    return render(request, "skills.html", context)