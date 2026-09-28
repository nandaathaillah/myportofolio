from datetime import datetime

from django.shortcuts import render
from django.template import context


from main.forms import AwardForm
from main.models import Experience, Award, Skill

from django.core.management import call_command
from django.http import HttpResponse, request, response

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Skill
from main.forms import SkillForm
from django.http import HttpResponse
from django.core import serializers

from main.forms import ExperienceForm


from django.contrib.auth.decorators import login_required  
from django.core.exceptions import PermissionDenied        



def show_main(request):
    last_login = request.COOKIES.get('last_login', 'No active login session / Cookie not found')

    context = {
        "name": "Nanda Athaillah Nurano",
        "npm": "2506557425",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "A Computer Science student at Universitas Indonesia interested "
            "in software development and education."
        ),
        "last_login": last_login,

    }

    return render(request, "index.html", context)


def show_experience(request):
    query =request.GET.get('q')
    
    if query:
        experience_list = Experience.objects.filter(title__icontains=query) | Experience.objects.filter(description__icontains=query)
    else:
        experience_list = Experience.objects.all()

    context = {
        "name": "Nanda Athaillah Nurano",
        "experience_list": experience_list, 
        "query": query if query else "",
    }
    return render(request, "experience.html", context)

@login_required(login_url="/login/")  
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = ExperienceForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_experience')
    context = {
            "name": "Nanda Athaillah Nurano",
            "form": form,
        }
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")  
def edit_experience(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied

    # Grab the exact experience by its UUID
    experience = get_object_or_404(Experience, pk=id)

    form = ExperienceForm(request.POST or None, instance=experience)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_experience')
    context = {
        "name": "Nanda Athaillah Nurano",
        "form": form,
    }
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")  
def delete_experience(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied

    experience = get_object_or_404(Experience, pk=id)
    if request.method == "POST":
        experience.delete()
    return redirect('main:show_experience')






def show_skills(request):
    # Grab whatever the user typed in the search box
    query = request.GET.get('q')
    skills = Skill.objects.all()

    if query:
        skills = Skill.objects.filter(category__icontains=query) | Skill.objects.filter(items__icontains=query)
    else:
        skills = Skill.objects.all()

    
    context = {
        "skills": skills,
        "name": "Nanda Athaillah Nurano"
    }
    return render(request, "skills.html", context)

@login_required(login_url="/login/")  
def load_my_data(request):
    try:
        # This mimics typing 'python manage.py loaddata' in the terminal
        call_command('loaddata', 'main_data.json')
        return HttpResponse("Data successfully loaded! You can go check your portfolio now.")
    except Exception as e:
        return HttpResponse(f"Uh oh, something went wrong: {e}")

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

@login_required(login_url="/login/")
def delete_award(request, award_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    award = get_object_or_404(Award, pk=award_id)
    if request.method == "POST":
        award.delete()
        messages.success(request, "Award berhasil dihapus!")
        return redirect("main:show_awards")
    return redirect("main:show_awards")

@login_required(login_url="/login/")  
def create_award(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = AwardForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Award baru berhasil ditambahkan!")
        return redirect("main:show_awards")

    context = {
        "name": "Nanda Athaillah Nurano",
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

@login_required(login_url="/login/")  
def edit_award(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied

    # Grab the specific award you want to edit
    award = get_object_or_404(Award, pk=id)
    
    # Put the award's old meat into the form. 
    # If the user pressed submit (POST), put the NEW meat in instead!
    form = AwardForm(request.POST or None, instance=award)
    
    #  If they submitted new meat and it's valid, save it!
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_awards')
        
    # If they just clicked "Edit", show them the page with the filled boxes
    context = {
            "name": "Nanda Athaillah Nurano",
            "form": form,
        }   
    return render(request, "edit_award.html", context)

@login_required(login_url="/login/")  
def create_skill(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = SkillForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_skills') 
    context = {
            "name": "Nanda Athaillah Nurano",
            "form": form,
        }
    return render(request, "skill_form.html", context)

@login_required(login_url="/login/")  
def edit_skill(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied

    skill = get_object_or_404(Skill, pk=id)
    form = SkillForm(request.POST or None, instance=skill)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_skills')
    return render(request, "edit_skill.html", {'form': form})

@login_required(login_url="/login/")  
def delete_skill(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied

    skill = get_object_or_404(Skill, pk=id)
    if request.method == "POST":
        skill.delete()
    return redirect('main:show_skills')

def show_json_skill(request):
    data = Skill.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")




def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect("main:login")

    context = {
        "name": "Nanda Athaillah Nurano",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Nanda Athaillah Nurano",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response



@login_required(login_url="/login/")
def toggle_star_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        # If this account has already starred it, remove the star.
        # If not, add one.
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")

@login_required(login_url="/login/")
def toggle_star_award(request, award_id):
    award = get_object_or_404(Award, pk=award_id)
    if request.method == "POST":
        if request.user in award.starred_by.all():
            award.starred_by.remove(request.user)
        else:
            award.starred_by.add(request.user)
    return redirect("main:show_awards")

@login_required(login_url="/login/")
def toggle_star_skill(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)
    if request.method == "POST":
        if request.user in skill.starred_by.all():
            skill.starred_by.remove(request.user)
        else:
            skill.starred_by.add(request.user)
    return redirect("main:show_skills")