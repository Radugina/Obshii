import requests


class ProjectApi:
    def __init__(self, url) -> None:
        self.url = url

    def get_token(self, login='mariiapravda1990@gmail.com', password='Ntcnbhjdobr1@', companyId="736ee6f7-c9ba-471c-b028-f020915a22fb"):
        creds = {
            "login": login,
            "password": password,
            "companyId": companyId
        }
        resp = requests.post(self.url + 'auth/keys', json=creds)
        return resp.json()["user_token"]

    def create_project(self, users):
        projects = {
            "name": "Учеба",
            "users": {"040ffab8-6e5c-4f4b-84ec-d0cbe18a66a1": "worker"}
        }
        resp = requests.post(self.url + 'projects', json=projects)
        return resp.json()

    def edit_project(self, users):
        projects = {
            "new_name": "Учеба2",
            "users": {"040ffab8-6e5c-4f4b-84ec-d0cbe18a66a1": "worker"}
        }
        resp = requests.put(self.url + 'projects/{id}', json=projects)
        return resp.json()

    def get_project(self, id):
        resp = requests.get(self.url + 'projects' + str(id))
        return resp.json()
