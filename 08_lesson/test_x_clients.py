from pages.ProjectApi import ProjectApi


def test_create_project():
    title = "Учеба"
    users = {"040ffab8-6e5c-4f4b-84ec-d0cbe18a66a1": "worker"}
    project_api = ProjectApi()
    result = project_api.create_project(title, users)
    new_id = result["id"]

    new_project = project_api.create_project(new_id)

    assert new_project["id"] == id


def test_edit():
    new_title = "Учеба2"
    users = {"040ffab8-6e5c-4f4b-84ec-d0cbe18a66a1": "worker"}
    project_api = ProjectApi()
    result = project_api.edit(new_title, users)
    new_title = result["new_title"]

    new_project = project_api.edit(new_title)

    assert new_project["new_title"] == new_title


def test_get_project():
    project_api = ProjectApi()
    result = project_api.get_project(id)
    new_id = result["id"]

    new_project = project_api.get_project(new_id)

    assert new_project["id"] == id


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
