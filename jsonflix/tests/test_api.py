from django.urls import reverse


def test_status_code(client, db):
    response = client.get(reverse('api'))
    assert response.status_code == 200
