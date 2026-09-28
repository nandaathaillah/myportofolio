import uuid

from django.contrib.auth.models import User  
from django.db import models



class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ("internship", "Internship"),
        ("research", "Research"),
        ("volunteer", "Volunteer"),
        ("part-time", "Part-Time"),
        ("full-time", "Full-Time"),
        ("freelance", "Freelance"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=EXPERIENCE_CHOICES,
        default="full-time",
    )
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    is_ongoing = models.BooleanField(default=True)
    starred_by = models.ManyToManyField(User, related_name="starred_experiences", blank=True)
    def __str__(self):
        return self.title


class Award(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    year = models.CharField(max_length=4)
    time_added = models.DateTimeField(auto_now_add=True)
    starred_by = models.ManyToManyField(User, related_name="starred_awards", blank=True)


class Skill(models.Model):
    category = models.CharField(max_length=100) # TODO: Delete  e.g., "Programming", "Languages"
    items = models.TextField() # TODO: Delete e.g., "C, C++, Java"
    time_added = models.DateTimeField(auto_now_add=True)
    starred_by = models.ManyToManyField(User, related_name="starred_skills", blank=True)
    