from django.forms import ModelForm, TextInput, Textarea
from main.models import Award

class AwardForm(ModelForm):
    class Meta:
        model = Award
        # Only ask for fields that ACTUALLY exist in your Award model!
        fields = [
            "title",
            "description",
            "year",
        ]
        
        labels = {
            "title": "Nama Penghargaan",
            "description": "Deskripsi",
            "year": "Tahun",
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
                    "placeholder": "Ceritakan tentang penghargaan ini...",
                    "rows": 3,
                }
            ),
            "year": TextInput(
                attrs={
                    "placeholder": "2023",
                }
            ),
        }