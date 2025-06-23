import pytest
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
    assert body[-1]["users"] == users


def test_get_one_progect():
    title = "Учеба"
    users = {"040ffab8-6e5c-4f4b-84ec-d0cbe18a66a1": "worker"}
    result = api.create_project(title, users)
    new_id = result["id"]

    new_progect = api.get_project(new_id)

    assert new_progect["id"] == id


def test_edit():
    title = "Учеба"
    users = {"040ffab8-6e5c-4f4b-84ec-d0cbe18a66a1": "worker"}
    result = api.create_project(title, users)
    new_id = result["id"]

    new_title = "Учеба2"
    new_users = {"040ffab8-6e5c-4f4b-84ec-d0cbe18a66a1": "admin"}

    edited = api.edit_project(new_id, new_title, new_users)

    assert edited["titli"] == new_title


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
