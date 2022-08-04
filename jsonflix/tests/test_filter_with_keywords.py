import requests


def test_filter_with_keywords():
    response = requests.get("http://127.0.0.1:8000/api/v1/?type=movie&description=Garfield,superheroes")
    response_body = response.json()
    for field in response_body:
        assert field["title"] == "Garfield's Pet Force"
