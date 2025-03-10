import requests

base_url = "https://ru.yougile.com"


def test_id_companies(login='', password='',):
    body = {
        "login": login,
        "password": password
    }
    header = {
      "Content-Type": "application/json"
    }
    company = requests.post(base_url+'/api-v2/auth/companies', json=body, headers= header)
    company.json()
    print(company.json())
    assert company.status_code == 200


def test_auth(login='', password='',
                  companyId= '11f0e61a-92b5-4904-b2a6-053d90f0c8c2'):
    body = {
    "login": login,
    "password": password,
    "companyId": companyId
     }
    header = {
     "Content-Type": "application/json"
    }
    resp = requests.post(base_url + '/api-v2/auth/keys', json=body, headers= header)
    print(resp.json())
    assert resp.status_code == 201


def test_get_projects():
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer "
    }
    resp = requests.get(base_url + 'api-v2/projects/{id}', headers=header)
    assert resp.status_code == 200
    print(resp.json())


def test_create_projects():
    body = {
   "title": "СОЛНЫШКО"
}
    header = {
     "Content-Type": "application/json",
     "Authorization": "Bearer "
    }
    projects = requests.put(base_url + 'api-v2/projects/{id}', json=body, headers= header)
    print(projects.json())


def test_change_projects():
    body = {
   "title": "Тестирование"
}
    header = {
     "Content-Type": "application/json",
     "Authorization": "Bearer "
    }
    change_projects = requests.post(base_url + '/api-v2/projects', json=body, headers= header)
    print(change_projects.json())


def test_receive_id():
    header = {
     "Content-Type": "application/json",
     "Authorization": "Bearer "
    }
    projects_id = requests.get(base_url + '/api-v2/projects/5796e5ab-0d70-4c7d-ba41-28677319b26b',
                                headers= header)
    print(projects_id.json())
    assert projects_id.status_code == 200
