import pytest
from ProjectApi import ProjectApi

api = ProjectApi("https://ru.yougile.com/api-v2/")


@pytest.fixture
def test_add_new():
    body = api.get_project_list()
    len_before = len(body)
    name = "Учеба"
    api.create_project(name)

    body = api.get_project_list()
    len_after = len(body)

    assert len_after - len_before == 1
    assert body[-1]["name"] == name


# Тест неудачного создания проекта (например, пустое название)
def test_edit_project_negative(self, headers):
    response = requests.post(api, json={}, headers=headers)
    assert response.status_code == 400  # Ошибка Bad Request


def test_edit():
    name = "Учеба"
    result = api.create_project(name)
    new_id = result["id"]

    new_name = "Учеба2"

    edited = api.edit_project(new_id, new_name)
    assert edited["name"] == new_name


# Тест попытки получить проект с неверным id
def test_id_project_negative(self, headers):
    response = requests.get("api/{non_existent_id}", headers=headers)
    assert response.status_code == 404  # ID не найден


def test_get_one_progect():
    name = "Учеба"
    result = api.create_project(name)
    new_id = result["id"]

    new_project = api.get_project(new_id)

    assert new_project["name"] == name
    assert new_project["is_active"] is True


# Тест попытки получить несуществующий проект
def test_get_project_negative(self, headers):
    response = requests.put("api/{non_existent_id}", headers=headers)
    assert response.status_code == 404  # Проект не найден
