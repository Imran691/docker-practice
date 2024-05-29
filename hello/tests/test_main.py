# from sqlmodel import create_engine, Session
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app = app)

# def client():
#     with app.test_client() as client:
#         yield client

def test_greet():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message" : "Hello World"}

def test_greet_1():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello" : "World"}

def test_greet_again():
    response = client.get('/who/World')
    assert response.status_code == 200
    assert response.json() == {"Hello World"}