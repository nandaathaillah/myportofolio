from django.urls import path
from main.views import (
    create_award_ajax, create_skill_ajax, create_experience_ajax,
    delete_award, delete_skill, delete_experience,
    edit_award_ajax, edit_experience_ajax, edit_skill_ajax,
    get_awards_json, get_skills_json, get_experiences_json,
    show_main, show_experience, show_awards, show_skills,
    toggle_star_award, toggle_star_experience, toggle_star_skill,
    register, login_user, logout_user
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('awards/', show_awards, name='show_awards'),
    path('skills/', show_skills, name='show_skills'),

    path("awards/<str:award_id>/delete/", delete_award, name="delete_award"),

    path("skills/<str:id>/delete/", delete_skill, name="delete_skill"),

    path('experience/', show_experience, name='show_experience'),
    path('experience/<str:id>/delete/', delete_experience, name='delete_experience'),

    path('register/', register, name='register'),
    path('login/', login_user, name='login'), 
    path("logout/", logout_user, name="logout"),
    
    path("experience/<uuid:experience_id>/star/", toggle_star_experience, name="toggle_star_experience"),
    path("awards/<str:award_id>/star/", toggle_star_award, name="toggle_star_award"),
    path("skills/<str:skill_id>/star/", toggle_star_skill, name="toggle_star_skill"),

    path("experience/json/", get_experiences_json, name="get_experiences_json"),
    path("experience/add/", create_experience_ajax, name="create_experience_ajax"),
    path("awards/add/", create_award_ajax, name="create_award_ajax"),
    path("awards/json/", get_awards_json, name="get_awards_json"),
    path("skills/json/", get_skills_json, name="get_skills_json"),
    path("skills/add/", create_skill_ajax, name="create_skill_ajax"),

    path('experience/<uuid:id>/edit-ajax/', edit_experience_ajax, name='edit_experience_ajax'),
    path('awards/<str:id>/edit-ajax/', edit_award_ajax, name='edit_award_ajax'),
    path('skills/<str:id>/edit-ajax/', edit_skill_ajax, name='edit_skill_ajax'),
]