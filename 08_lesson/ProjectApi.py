import requests
from config import MY_CREDS


class ProjectApi:
    def __init__(self, url) -> None:
        self.url = url
        self.headers = {"Authorization": f"Bearer {self.get_token()}"}

    def get_project_list(self, params_to_add=None):
        resp = requests.get(
            self.url + 'projects/list', headers=self.headers,
            params=params_to_add)
        return resp.json()

    def get_token(self):
        creds = MY_CREDS
        resp = requests.post(self.url + 'auth/keys', json=creds)
        return resp.json()["key"]

    def create_project(self):
        projects = {
            "title": self.title,
            "users": self.users
        }
        resp = requests.post(
            self.url + 'projects', json=projects, headers=self.headers)
        return resp.json()["id"]

    def get_project(self):
        projects = {
            "deleted": True,
            "title": self.title,
            "users": self.users
        }
        resp = requests.get(
            self.url + 'projects/' + str(id), json=projects,
            headers=self.headers)
        return resp.json()

    def edit_project(self):
        projects = {
            "title": self.new_title,
            "users": self.users
        }
        resp = requests.put(
            self.url + 'projects/' + str(id), json=projects,
            headers=self.headers)
        return resp.json()["id"]

    def create_project_negativ(self, title, users):
        projects = {
            "title": title,
            "users": users
        }
        resp = requests.post(
            self.url + 'projects', json=projects,
            headers=self.headers)
        return resp.status_code == 400

    def project_id_negativ(self, title, users):
        projects = {
            "deleted": False,
            "title": title,
            "users": users
        }
        resp = requests.get(
            self.url + 'projects/' + str(id), json=projects,
            headers=self.headers)
        return resp.status_code == 400

    def get_project_negative(self, title, users):
        projects = {
            "title": title,
            "users": users
        }
        resp = requests.put(
            self.url + 'projects/' + str(id), json=projects,
            headers=self.header)
        return resp.status_code == 400
