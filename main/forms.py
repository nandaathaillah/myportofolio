from django.forms import ModelForm, Select, TextInput, Textarea
from main.models import Award, Skill, Experience  

class AwardForm(ModelForm):
    class Meta:
        model = Award
        fields = [
            "title",
            "description",
            "year",
        ]
        
        labels = {
            "title": "Award name",
            "description": "Description",
            "year": "Year",
        }
        
        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Silver Medalist - Microsoft Excel",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Describe this award...",
                    "rows": 3,
                }
            ),
            "year": TextInput(
                attrs={
                    "placeholder": "2023",
                }
            ),
        }

    from main.models import Skill # Add Skill to your imports at the top!

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ["category", "items"]
        labels = {
            "category": "Skill Category",
            "items": "Skill Items",
        }
        widgets = {
            "category": TextInput(attrs={"placeholder": "Programming, Languages, etc.", "maxlength": 100}),
            "items": Textarea(attrs={"placeholder": "C, C++, Java", "rows": 3}),
        }


class ExperienceForm(ModelForm):
    class Meta:
        model=Experience
        fields = ["title", "category", "description", "is_ongoing"] 
        labels = {
            "title": "Experience Title",
            "category": "Category",
            "description": "Description",
            "is_ongoing": "Is this experience ongoing?",
        }  

        Widgets ={
            "category": Select(attrs={"class": "form-select"}),
            "is_ongoing": Select(choices=[(True, 'Yes (Ongoing)'), (False, 'No (Completed)')], attrs={"class": "form-select"})
        }