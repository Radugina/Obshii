import requests


class ProjectApi:
    def __init__(self, url) -> None:
        self.url = url

    def get_project_list(self, params_to_add=None):
        resp = requests.get(self.url + '/projects/list', params=params_to_add)
        return resp.json()

    def get_token(self):
        creds = {
            "login": 'mariiapravda1990@gmail.com',
            "password": 'Ntcnbhjdobr1@',
            "companyId": "736ee6f7-c9ba-471c-b028-f020915a22fb"
        }
        resp = requests.post(self.url + 'auth/keys', json=creds)
        return resp.json()["user_token"]

    def create_project(self, title, users):
        projects = {
            "title": title,
            "users": users
        }
        resp = requests.post(self.url + 'projects', json=projects)
        return resp.json()

    def get_project(self, id):
        resp = requests.get(self.url + 'projects/' + str(id))
        return resp.json()

    def edit_project(self, new_title, users):
        client_token = self.get_token()
        url_with_token = f"{self.url}/projects/{id}?client_token={client_token}"
        projects = {
            "new_title": new_title,
            "users": users
        }
        resp = requests.put(url_with_token, json=projects)
        return resp.json()

    def create_project_negativ(self, title, users):
        projects = {
            "title": title,
            "users": users
        }
        resp = requests.post(self.url + 'projects', json=projects)
        return resp.status_code == 401

    def project_title_negativ(self, title, users):
        resp = requests.get(self.url + 'projects/' + str(6767676767676))
        return resp.status_code == 401

    def get_project_negative(self, new_title, users):
        client_token = self.get_token()
        url_with_token = f"{self.url}/projects/{id}?client_token={client_token}"
        projects = {
            "new_title": new_title,
            "users": users
        }
        resp = requests.put(url_with_token, json=projects)
        return resp.status_code == 401
