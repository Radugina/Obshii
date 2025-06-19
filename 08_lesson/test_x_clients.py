import pytest
import requests
from ProjectApi import ProjectApi

api = ProjectApi("https://ru.yougile.com/api-v2/")


@pytest.fixture
def test_add_new():
    body = api.get_project_list()
    len_before = len(body)
    title = "Учеба"
    users = {"040ffab8-6e5c-4f4b-84ec-d0cbe18a66a1": "worker"}
    api.create_project(title, users)

    body = api.get_project_list()
    len_after = len(body)

    assert len_after - len_before == 1
    assert body[-1]["title"] == title
    assert body[-1]["users"] == {"040ffab8-6e5c-4f4b-84ec-d0cbe18a66a1": "worker"}


def test_get_one_progect():
    title = "Учеба"
    users = {"040ffab8-6e5c-4f4b-84ec-d0cbe18a66a1": "worker"}
    result = api.create_project(title, users)
    new_id = result["id"]

    new_project = api.get_project(new_id)

    assert new_project["title"] == title
    assert new_project["users"] == users
    assert new_project["is_active"] is True


def test_edit():
    title = "Учеба"
    users = {"040ffab8-6e5c-4f4b-84ec-d0cbe18a66a1": "worker"}
    result = api.create_project(title, users)
    new_id = result["id"]

    new_title = "Учеба2"
    new_id = {"5f879c26-9421-4732-9104-ae0d0060e655"}

    edited = api.edit_project(new_id, new_title)
    assert edited["title"] == new_title
    assert edited["id"] == new_id


# Тест неудачного создания проекта (например, пустое название)
def test_edit_project_negative():
    title = " "
    users = {"040ffab8-6e5c-4f4b-84ec-d0cbe18a66a1": "worker"}
    response = requests.post("https://ru.yougile.com/api-v2/projects")
    assert response.status_code == 401


# Тест попытки получить проект с неверным id
def test_id_project_negative():
    project_id = "non_existent_project_id"
    projects = {"title": "Обновленное название проекта"}
    response = requests.get("https://ru.yougile.com/api-v2/projects")
    assert response.status_code == 401


# Тест попытки получить несуществующий проект
def test_get_project_negative():
    project_id = "non_existent_project_id"
    response = requests.put("https://ru.yougile.com/api-v2/projects")
    assert response.status_code == 401
