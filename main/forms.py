from django.forms import ModelForm, Select, TextInput, Textarea
from main.models import Award, Skill, Experience  
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags
from django.forms import ModelForm

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

    from main.models import Skill # Add Skill to your imports at the top

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

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Experience title can't contain only HTML tags.")
        return title

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()