from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


client = Client()


def test_home_index():
    response = client.get(reverse('home:index'))
    content = response.content.decode("utf-8")
    assert response.status_code == 200
    assert "<title>Holiday Homes</title>" in content
    assertTemplateUsed(response, "home/index.html")
