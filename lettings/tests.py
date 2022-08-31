from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
import pytest
from lettings.models import Letting, Address


client = Client()


@pytest.mark.django_db
def test_lettings_index():
    response = client.get(reverse('lettings:index'))
    content = response.content.decode("utf-8")
    assert response.status_code == 200
    assert "<title>Lettings</title>" in content
    assertTemplateUsed(response, "lettings/index.html")


@pytest.mark.django_db
def test_lettings_lettings():
    Address.objects.create(
        number=888,
        street='a street',
        city="a city",
        state=" a state",
        zip_code=75000,
        country_iso_code="FR-fr"
    )
    address = Address.objects.all()[0]
    Letting.objects.create(
        title="test title",
        address=address,
    )
    response = client.get(reverse('lettings:letting', kwargs={"letting_id": 1}))
    content = response.content.decode("utf-8")
    assert "test title" in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")
