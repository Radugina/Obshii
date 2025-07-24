from ProjectApi import ProjectApi


def test_create_project():
    title = "Учеба"
    users = {"040ffab8-6e5c-4f4b-84ec-d0cbe18a66a1": "worker"}
    project_api = ProjectApi()
    result = project_api.create_project(title, users)

    assert "id" in result


def test_edit():
    project_api = ProjectApi()
    new_project = project_api.create_project("Учеба", "users")
    project_id = new_project["id"]
    updated_project = project_api.edit(project_id, "Учеба2", "users")

    assert updated_project.get("title") == "Учеба2"


def test_get_project():
    project_api = ProjectApi()
    new_project = project_api.create_project("Учеба", "users")
    project_id = new_project["id"]
    fetched_project = project_api.get_project(project_id)

    assert fetched_project["id"] == project_id


# Тест неудачного создания проекта (например, пустое название)
def test_project_negative():
    project_api = ProjectApi()
    result = project_api.create_project_negativ("", "users")
    assert result is True  # Проверяем статус 404


# Тест попытки получить проект с неверным id
def test_id_project_negative():
    project_api = ProjectApi()
    result = project_api.project_id_negativ("9999999999", "title", "users")
    assert result is True  # Проверяем статус 404


# Тест попытки получить несуществующий проект
def test_get_project_negative():
    project_api = ProjectApi()
    result = project_api.get_project_negative("VK", "users")
    assert result is True  # Проверяем статус 404
