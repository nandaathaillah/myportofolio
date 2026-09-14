from django.urls import path
from main.views import show_main, show_experience, show_awards, show_skills

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('experience/', show_experience, name='show_experience'),
    path('awards/', show_awards, name='show_awards'),
    path('skills/', show_skills, name='show_skills'),
]