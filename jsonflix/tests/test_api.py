import pytest
from django.urls import reverse
from jsonflix.models import Netflix


@pytest.fixture
def user():
    pass


def test_shows_list(client, db):
    response = client.get(reverse('api'))
    assert response.status_code == 200


def test_list_shows_description(client, db):
    Netflix.objects.create(
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
    )
    Netflix.objects.create(
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


def test_shows_limit(client, db):
    Netflix.objects.create(
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
    )
    Netflix.objects.create(
        id=2,
        type="TV Show",
        title="Blood & Water",
        director="",
        cast="Ama Qamata, Khosi Ngema, Gail Mabalane, Thabang Molaba, Dillon Windvogel, Natasha Thahane, Arno Greeff, Xolile Tshabalala, Getmore Sithole, Cindy Mahlangu, Ryle De Morny, Greteli Fincham, Sello Maake Ka-Ncube, Odwa Gwanya, Mekaila Mathys, Sandi Schultz, Duane Williams, Shamilla Miller, Patrick Mofokeng",
        country="South Africa",
        date_added="2021-09-24",
        release_year="2021",
        rating="TV-MA",
        duration="2 Seasons",
        genres="International TV Shows, TV Dramas, TV Mysteries",
        description="After crossing paths at a party, a Cape Town teen sets out to prove whether a private-school swimming star is her sister who was abducted at birth."
    )

    dados = {
        'limit': [1]
    }
    resp = client.get(reverse('api'), dados).json()

    assert len(resp) == 1