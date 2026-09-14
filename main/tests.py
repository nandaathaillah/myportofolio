from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience,Award,Skill


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="PBP Teaching Assistant",
            description="Help students understand web development.",
            category="part-time",
        )
        self.skill = Skill.objects.create(
            category="Programming",
            items="Python, JavaScript, HTML, CSS"
        )
        self.award = Award.objects.create(
            title="Silver Medalist",
            description="Microsoft Office Specialist National Championship",
            year="2023"
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')
        self.assertContains(response, f'href="{reverse("main:show_awards")}"')
        self.assertContains(response, f'href="{reverse("main:show_skills")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/a-page-that-does-not-exist/")

        self.assertEqual(response.status_code, 404)
    #Experience tests
    def test_experience_model(self):
        self.assertEqual(str(self.experience), "PBP Teaching Assistant")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Ongoing")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')
        self.assertContains(response, f'href="{reverse("main:show_awards")}"')
        self.assertContains(response, f'href="{reverse("main:show_skills")}"')  
    
    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "No experience has been added yet.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Completed")
        self.assertNotContains(response, "Ongoing")
    #Skills tests
    def test_empty_skills_page(self):
        Skill.objects.all().delete()
        response = self.client.get(reverse("main:show_skills"))

        self.assertContains(response, "No skills have been added yet.")

    def test_skills_page(self):
        response = self.client.get(reverse("main:show_skills"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skills.html")
        self.assertContains(response, self.skill.category)
        self.assertContains(response, self.skill.items)
        self.assertContains(response, f'href="{reverse("main:show_main")}"')
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')
        self.assertContains(response, f'href="{reverse("main:show_awards")}"')
        self.assertContains(response, f'href="{reverse("main:show_skills")}"')  
    #award
    def test_award_model(self):
        self.assertEqual(self.award.title, "Silver Medalist")
        self.assertEqual(self.award.year, "2023")

    def test_award_page(self):
        response = self.client.get(reverse("main:show_awards"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "awards.html")
        self.assertContains(response, self.award.title)
        self.assertContains(response, self.award.description)
        self.assertContains(response, f'href="{reverse("main:show_main")}"')
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')
        self.assertContains(response, f'href="{reverse("main:show_skills")}"')
        self.assertContains(response, f'href="{reverse("main:show_awards")}"')  
    
    def test_empty_award_page(self):
        Award.objects.all().delete()
        response = self.client.get(reverse("main:show_awards"))

        self.assertContains(response, "No awards have been added yet.")