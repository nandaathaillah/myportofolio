from django.urls import path
from main.views import show_main, show_experience, show_awards, show_skills
from main.views import show_main, show_experience, show_awards, show_skills, load_my_data

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('experience/', show_experience, name='show_experience'),
    path('awards/', show_awards, name='show_awards'),
    path('skills/', show_skills, name='show_skills'),
    path('secret-load-data/', load_my_data, name='load_my_data'), # Your secret trigger!
]