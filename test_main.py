from pydoc import cli
from urllib import response
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_create_todo():
    response = client.post(
        "/",
        json={ "name": "string",
                "description": "string",
                "completed": True,
                "date": "string"
            }
    )
    assert response.status_code == 200
    test_out = response.json()[0]
    global test_id
    test_id = test_out['id']
    assert test_out["name"] == "string"
    assert test_out["description"] == "string"
    assert test_out["completed"] == True
    assert test_out["date"] == "string"

def test_update_todo():
    stringexec = '/' + test_id
    response = client.put(stringexec,
        json={ "name": "string",
                "description": "string",
                "completed": False,
                "date": "string"
            })
    assert response.status_code == 200
    test_out = response.json()[0]
    assert test_out["completed"] == False


def test_delete_todo():
    stringexec = '/' + test_id
    response = client.delete(stringexec)
    assert response.status_code == 200

def test_get_todo():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == []