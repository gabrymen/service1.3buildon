import requests

BASE_URL = 'http://127.0.0.1:5000'

def test_index():
    response = requests.get(f'{BASE_URL}/')
    assert response.status_code == 200
    print(response.json())

def test_preprocess():
    data = {"data": [[1, 2, 3], [4, 5, 6]]}
    response = requests.post(f'{BASE_URL}/api/preprocess', json=data)
    assert response.status_code == 200
    print(response.json())

def test_cluster():
    data = {"data": [[1, 2, 3], [4, 5, 6]]}
    response = requests.post(f'{BASE_URL}/api/cluster', json=data)
    assert response.status_code == 200
    print(response.json())

if __name__ == '__main__':
    test_index()
    test_preprocess()
    test_cluster()
