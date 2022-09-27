from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
import pytest
from profiles.models import Profile
from django.contrib.auth import get_user_model


client = Client()
User = get_user_model()


@pytest.mark.django_db
def test_profiles_index():
    response = client.get(reverse('profiles:index'))
    content = response.content.decode("utf-8")
    assert response.status_code == 200
    assert "<title>Profiles</title>" in content
    assertTemplateUsed(response, "profiles/index.html")


@pytest.mark.django_db
def test_profiles_profile():
    user = User.objects.create(
        username="testuser",
        password="testpass1",
    )
    Profile.objects.create(
        user=user,
        favorite_city="my favorite city"
    )
    profile = Profile.objects.all()[0]
    assert profile.user.username == "testuser"
    response = client.get(reverse('profiles:profile', kwargs={"username": "testuser"}))
    content = response.content.decode("utf-8")
    assert "testuser" in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")
