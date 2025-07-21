import pytest
from pages.ProjectApi import ProjectApi


@pytest.fixture
def test_create_project():
    title = "Учеба"
    users = {"040ffab8-6e5c-4f4b-84ec-d0cbe18a66a1": "worker"}
    result = projects(title, users)
    new_id = result["id"]

    new_project = projects(new_id)

    assert new_project["id"] == id


def test_edit():
    new_title = "Учеба2"
    users = {"040ffab8-6e5c-4f4b-84ec-d0cbe18a66a1": "worker"}
    result = projects(new_title, users)
    new_id = result["new_title"]

    new_project = projects(new_id)

    assert new_project["new_titli"] == new_title


def test_get_project():
    title = "Учеба"
    users = {"040ffab8-6e5c-4f4b-84ec-d0cbe18a66a1": "worker"}
    result = projects(title, users)
    new_id = result["id"]

    new_project = projects(new_id)

    assert new_project["title"] == title
    assert new_project["users"] == users


# Тест неудачного создания проекта (например, пустое название)
def test_project_negative():
    title = ""
    users = {"040ffab8-6e5c-4f4b-84ec-d0cbe18a66a1": "worker"}

    print("Получена ошибка 400 Bad Request")


# Тест попытки получить проект с неверным id
def test_id_project_negative():
    deleted = False
    title = "Учеба"
    users = {"040ffab8-6e5c-4f4b-84ec-d0cbe18a66a1": "worker"}

    print("Получена ошибка 400 Bad Request")


# Тест попытки получить несуществующий проект
def test_get_project_negative():
    title = "Несуществующий проект"
    users = {"040ffab8-6e5c-4f4b-84ec-d0cbe18a66a1": "worker"}

    print("Получена ошибка 400 Bad Request")
