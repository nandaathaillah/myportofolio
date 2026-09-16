from django.shortcuts import render
from django.template import context

from main.forms import AwardForm
from main.models import Experience
from .models import Experience, Award, Skill

from django.core.management import call_command
from django.http import HttpResponse, request, request

from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render



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
    json_response = get_awards_json(request)
    awards = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    awards = [award.object for award in awards]
    title_query = request.GET.get("title", "").strip()
    context = {
        "name": "Nanda Athaillah Nurano",
        "award_list": awards,
        "title_query": title_query,
    }

    return render(request, "awards.html", context)

def delete_award(request, award_id):
    award = get_object_or_404(Award, pk=award_id)
    if request.method == "POST":
        award.delete()
        messages.success(request, "Award berhasil dihapus!")
        return redirect("main:show_awards")
    return redirect("main:show_awards")

def show_skills(request):
    skills = Skill.objects.all()
    context = {
        "skill_list": skills,
        "name": "Nanda Athaillah Nurano"
    }
    return render(request, "skills.html", context)

def load_my_data(request):
    try:
        # This mimics typing 'python manage.py loaddata' in the terminal
        call_command('loaddata', 'main_data.json')
        return HttpResponse("Data successfully loaded! You can go check your portfolio now.")
    except Exception as e:
        return HttpResponse(f"Uh oh, something went wrong: {e}")

def create_award(request):
    form = AwardForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Award baru berhasil ditambahkan!")
        return redirect("main:show_awards")

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "awards_form.html", context)

def get_awards_json(request):
    title_query = request.GET.get("title", "").strip()
    awards = Award.objects.all()
    
    # If user searched for something, filter it
    if title_query:
        awards = awards.filter(title__icontains=title_query)
        
    awards_json = serializers.serialize("json", awards)
    return HttpResponse(awards_json, content_type="application/json")