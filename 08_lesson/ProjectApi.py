import requests
from config import MY_CREDS, API_BASE_URL


class ProjectApi:
    def __init__(self):
        self.url = API_BASE_URL
        self.headers = {"Authorization": f"Bearer {self.get_token()}"}

    def get_token(self):
        creds = MY_CREDS
        resp = requests.post(self.url + 'auth/keys', json=creds)
        return resp.json()["key"]

    def create_project(self, title, users):
        projects = {
            "title": title,
            "users": users
        }
        resp = requests.post(
            self.url + 'projects', json=projects, headers=self.headers)
        return resp.json()

    def edit(self, project_id, new_title, users):
        projects = {
            "project_id": project_id,
            "new_title": new_title,
            "users": users
        }
        resp = requests.put(
            self.url + 'projects/' + str(project_id), json=projects,
            headers=self.headers)
        return resp.json()["id"]

    def get_project(self, id):
        resp = requests.get(
            self.url + 'projects/' + str(id),
            headers=self.headers)
        return resp.json()

    def create_project_negativ(self, title, users):
        projects = {
            "title": title,
            "users": users
        }
        resp = requests.post(
            self.url + 'projects', json=projects,
            headers=self.headers)
        return resp.status_code == 404

    def project_id_negativ(self, project_id, title, users):
        projects = {
            "project_id": project_id,
            "title": title,
            "users": users
        }
        resp = requests.get(
            self.url + 'projects', json=projects,
            headers=self.headers)
        return resp.status_code == 404

    def get_project_negative(self, title, users):
        projects = {
            "title": title,
            "users": users
        }
        resp = requests.put(
            self.url + 'projects', json=projects,
            headers=self.headers)
        return resp.status_code == 404
