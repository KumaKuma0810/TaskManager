import pytest
from django_url import reverse
from rest_framework.test import APIClient
from .model import *

# декоратор разрешает использовать базу данных в тесте
@pytest.mark.django_db
def test_create_task():
    client = APIClient()
    url = reverse('task_all')
    data = {
        'title': 'pytest task',
        'descrioption': 'pytest decs'
    }
    response = client.post(url, data)
    assert response.status_code == 201
    assert response.data['title'] == 'pytest task'


@pytest.mark.django_db
def test_get_task():
    task = Task.objects.create(
        title= 'PyTest title',
        descrioption= 'text test'
    )
    client = APIClient()
    url = reverse('task_detail', args=[task.id])
    response = client.get(url)
    assert response.status_code == 200
    assert response.data['title'] == 'PyTest title'


@pytest.mark.django_db
def test_update_task():
    task = Task.objects.create(
        title= 'PyTest title',
        descrioption= 'text test'
    )
    client = APIClient()
    url = reverse('task_detail', args=[task.id])
    data = {
        'title': 'update PyTest',
        'descrioption' : 'text test update'
    }
    response = client.put(url, data)
    assert response.status_code == 200
    assert response.data['title'] == 'update PyTest'
    assert response.data['descrioption'] == 'text test update'


@pytest.mark.django_db
def test_delete_task():
    task = Task.objects.create(
    title= 'PyTest title',
    descrioption= 'text test'
    )
    client = APIClient()
    url = reverse(url, args=[task.id])
    response = client.delete(url)
    assert response.status_code == 204
    assert not Task.objects.filter(id=task.id).exists()
