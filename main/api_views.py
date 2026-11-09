from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import (
    api_view, authentication_classes, permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import Experience
from main.permissions import IsPortfolioOwnerOrReadOnly
from main.serializers import ExperienceSerializer

from main.models import Experience, Award, Skill
from main.serializers import ExperienceSerializer, AwardSerializer, SkillSerializer
from main.permissions import IsPortfolioOwnerOrReadOnly, IsPortfolioOwnerOrEditorOrReadOnly

@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrReadOnly])
def experience_list(request):
    if request.method in ("GET", "HEAD"):
        experiences = Experience.objects.prefetch_related("starred_by").order_by("title", "id")
        title = request.query_params.get("title", "").strip()
        if title:
            experiences = experiences.filter(title__icontains=title)
        
        serializer = ExperienceSerializer(
            experiences, many=True, context={"request": request},
        )
        return Response(serializer.data)

    serializer = ExperienceSerializer(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrReadOnly])
def experience_detail(request, experience_id):
    experience = get_object_or_404(
        Experience.objects.prefetch_related("starred_by"), pk=experience_id,
    )

    if request.method in ("GET", "HEAD"):
        serializer = ExperienceSerializer(experience, context={"request": request})
        return Response(serializer.data)

    if request.method == "DELETE":
        experience.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = ExperienceSerializer(
        experience, data=request.data, partial=request.method == "PATCH",
        context={"request": request},
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def experience_star(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    
    if experience.starred_by.filter(pk=request.user.pk).exists():
        experience.starred_by.remove(request.user)
    else:
        experience.starred_by.add(request.user)
        
    serializer = ExperienceSerializer(experience, context={"request": request})
    return Response(serializer.data)

#Awards API views
@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def award_list(request):
    if request.method in ("GET", "HEAD"):
        awards = Award.objects.prefetch_related("starred_by").order_by("-year", "id")
        title = request.query_params.get("title", "").strip()
        if title:
            awards = awards.filter(title__icontains=title)
        
        serializer = AwardSerializer(awards, many=True, context={"request": request})
        return Response(serializer.data)

    if not request.user.is_superuser:
        return Response({"detail": "Only the owner can create awards."}, status=status.HTTP_403_FORBIDDEN)

    serializer = AwardSerializer(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def award_detail(request, award_id):
    award = get_object_or_404(Award.objects.prefetch_related("starred_by"), pk=award_id)

    if request.method in ("GET", "HEAD"):
        serializer = AwardSerializer(award, context={"request": request})
        return Response(serializer.data)

    if request.method == "DELETE":
        if not request.user.is_superuser:
            return Response({"detail": "Only the owner can delete awards."}, status=status.HTTP_403_FORBIDDEN)
        award.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = AwardSerializer(
        award, data=request.data, partial=request.method == "PATCH",
        context={"request": request}
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def award_star(request, award_id):
    award = get_object_or_404(Award, pk=award_id)
    if award.starred_by.filter(pk=request.user.pk).exists():
        award.starred_by.remove(request.user)
    else:
        award.starred_by.add(request.user)
    serializer = AwardSerializer(award, context={"request": request})
    return Response(serializer.data)

#skills api views
@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def skill_list(request):
    if request.method in ("GET", "HEAD"):
        skills = Skill.objects.prefetch_related("starred_by").order_by("category", "id")
        q = request.query_params.get("q", "").strip()
        if q:
            skills = skills.filter(items__icontains=q)
        
        serializer = SkillSerializer(skills, many=True, context={"request": request})
        return Response(serializer.data)

    if not request.user.is_superuser:
        return Response({"detail": "Only the owner can create skills."}, status=status.HTTP_403_FORBIDDEN)

    serializer = SkillSerializer(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def skill_detail(request, skill_id):
    skill = get_object_or_404(Skill.objects.prefetch_related("starred_by"), pk=skill_id)

    if request.method in ("GET", "HEAD"):
        serializer = SkillSerializer(skill, context={"request": request})
        return Response(serializer.data)

    if request.method == "DELETE":
        if not request.user.is_superuser:
            return Response({"detail": "Only the owner can delete skills."}, status=status.HTTP_403_FORBIDDEN)
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = SkillSerializer(
        skill, data=request.data, partial=request.method == "PATCH",
        context={"request": request}
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def skill_star(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)
    if skill.starred_by.filter(pk=request.user.pk).exists():
        skill.starred_by.remove(request.user)
    else:
        skill.starred_by.add(request.user)
    serializer = SkillSerializer(skill, context={"request": request})
    return Response(serializer.data)