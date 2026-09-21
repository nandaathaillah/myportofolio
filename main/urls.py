from django.urls import path
from main.views import create_award, create_skill, delete_award, delete_skill, edit_award, edit_skill, get_awards_json, show_json_skill, show_main, show_experience, show_awards, show_skills
from main.views import show_main, show_experience, show_awards, show_skills, create_experience, edit_experience, delete_experience

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('awards/', show_awards, name='show_awards'),
    path('skills/', show_skills, name='show_skills'),

    path("awards/add/", create_award, name="create_award"),
    path("api/awards/", get_awards_json, name="get_awards_json"),   
    path("awards/<str:award_id>/delete/", delete_award, name="delete_award"),
    path('awards/<str:id>/edit/', edit_award, name='edit_award'),

    path("skills/add/", create_skill, name="create_skill"),
    path("skills/<str:id>/edit/", edit_skill, name="edit_skill"),
    path("skills/<str:id>/delete/", delete_skill, name="delete_skill"),
    path("api/skills/", show_json_skill, name="show_json_skill"),

    
    path('experience/', show_experience, name='show_experience'),
    path("experience/add/", create_experience, name="create_experience"),
    path('experience/<str:id>/edit/', edit_experience, name='edit_experience'),
    path('experience/<str:id>/delete/', delete_experience, name='delete_experience'),
]