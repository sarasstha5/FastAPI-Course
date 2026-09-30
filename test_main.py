from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
#alwys put the function name starting from either "test..." or"_test..."" class name "Test..."
#test home api 
def test_home():
    response = client.get("/")
    #test status of home api
    assert response.status_code == 200
    #test return 
    assert response.json() == {"message":"testing the functions"}

#test for /add
def test_add():
    response = client.get("/add?a=4&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": 9}