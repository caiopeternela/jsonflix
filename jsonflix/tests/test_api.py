import pytest
import requests
from django.core.exceptions import ValidationError
from django.urls import reverse
from jsonflix.models import Netflix


@pytest.fixture
def shows(db):
    return Netflix.objects.bulk_create(
        [
            Netflix(
                id=22,
                type="TV Show",
                title="Resurrection: Ertugrul",
                director="",
                cast="Engin Altan Düzyatan, Serdar Gökhan, Hülya Darcan, Kaan Taşaner, Esra Bilgiç, Osman Soykut, Serdar Deniz, Cengiz Coşkun, Reshad Strik, Hande Subaşı",
                country="Turkey",
                date_added="2021-09-22",
                release_year="2018",
                rating="TV-14",
                duration="5 Seasons",
                genres="International TV Shows, TV Action & Adventure, TV Dramas",
                description="When a good deed unwittingly endangers his clan, a 13th-century Turkish warrior agrees to fight a sultan's enemies in exchange for new tribal land."
            ),
            Netflix(
                id=2,
                type="TV Show",
                title="Blood & Water",
                director="",
                cast='''"Ama Qamata, Khosi Ngema, Gail Mabalane, Thabang Molaba, Dillon Windvogel,
        Natasha Thahane, Arno Greeff, Xolile Tshabalala, Getmore Sithole, Cindy Mahlangu,
        Ryle De Morny, Greteli Fincham, Sello Maake Ka-Ncube, Odwa Gwanya, Mekaila Mathys,
        Sandi Schultz, Duane Williams, Shamilla Miller, Patrick Mofokeng"''',
                country="South Africa",
                date_added="2021-09-24",
                release_year="2021",
                rating="TV-MA",
                duration="2 Seasons",
                genres="International TV Shows, TV Dramas, TV Mysteries",
                description="After crossing paths at a party, a Cape Town teen sets out to prove whether a private-school swimming star is her sister who was abducted at birth."
            )
        ]
    )


def test_response_time():
    url = 'https://jsonflix.herokuapp.com/api/v1/all'
    response = requests.get(url)
    assert response.elapsed.total_seconds() < 5


def test_shows_list(client, db):
    response = client.get(reverse('api'))
    assert response.status_code == 200


def test_shows_type(client, shows):
    data = {
        'type': ['42']
    }
    response = client.get(reverse('api'), data).json()

    assert response == {
        'error': "Only 'movie' and 'tv_show' are accepted in the type field"
    }


def test_shows_release_year(client, shows):
    dados = {
        'release_year': ['2018,2019'],
        'description': ['fight,clan,warrior']
    }
    resp = client.get(reverse('api'), dados).json()

    assert resp == [
        {
            "id": 22,
            "type": "TV Show",
            "title": "Resurrection: Ertugrul",
            "director": "",
            "cast": "Engin Altan Düzyatan, Serdar Gökhan, Hülya Darcan, Kaan Taşaner, Esra Bilgiç, Osman Soykut, Serdar Deniz, Cengiz Coşkun, Reshad Strik, Hande Subaşı",
            "country": "Turkey",
            "date_added": "2021-09-22",
            "release_year": "2018",
            "rating": "TV-14",
            "duration": "5 Seasons",
            "genres": "International TV Shows, TV Action & Adventure, TV Dramas",
            "description": "When a good deed unwittingly endangers his clan, a 13th-century Turkish warrior agrees to fight a sultan's enemies in exchange for new tribal land."
        }
    ]


def test_list_shows_description(client, shows):
    dados = {
        'description': ['fight,clan,warrior']
    }
    resp = client.get(reverse('api'), dados).json()

    assert resp == [
        {
            "id": 22,
            "type": "TV Show",
            "title": "Resurrection: Ertugrul",
            "director": "",
            "cast": "Engin Altan Düzyatan, Serdar Gökhan, Hülya Darcan, Kaan Taşaner, Esra Bilgiç, Osman Soykut, Serdar Deniz, Cengiz Coşkun, Reshad Strik, Hande Subaşı",
            "country": "Turkey",
            "date_added": "2021-09-22",
            "release_year": "2018",
            "rating": "TV-14",
            "duration": "5 Seasons",
            "genres": "International TV Shows, TV Action & Adventure, TV Dramas",
            "description": "When a good deed unwittingly endangers his clan, a 13th-century Turkish warrior agrees to fight a sultan's enemies in exchange for new tribal land."
        }
    ]


def test_shows_limit(client, shows):
    dados = {
        'limit': [1]
    }
    resp = client.get(reverse('api'), dados).json()

    assert len(resp) == 1


def test_country_code(client, shows):
    data = {
        'country': ['TR']
    }
    response = client.get(reverse('api'), data).json()
    assert response == [
        {
            "id": 22,
            "type": "TV Show",
            "title": "Resurrection: Ertugrul",
            "director": "",
            "cast": "Engin Altan Düzyatan, Serdar Gökhan, Hülya Darcan, Kaan Taşaner, Esra Bilgiç, Osman Soykut, Serdar Deniz, Cengiz Coşkun, Reshad Strik, Hande Subaşı",
            "country": "Turkey",
            "date_added": "2021-09-22",
            "release_year": "2018",
            "rating": "TV-14",
            "duration": "5 Seasons",
            "genres": "International TV Shows, TV Action & Adventure, TV Dramas",
            "description": "When a good deed unwittingly endangers his clan, a 13th-century Turkish warrior agrees to fight a sultan's enemies in exchange for new tribal land."
        }
    ]
