import json

import pytest

from conftest import ClientQuery
from hospitals.models import Hospital


@pytest.fixture
def hospital() -> Hospital:
    return Hospital.objects.create(name="foo")


@pytest.fixture
def hospitals() -> list[Hospital]:
    h1 = Hospital.objects.create(name="foo")
    h2 = Hospital.objects.create(name="foo")
    return [h1, h2]


@pytest.mark.django_db
def test_hospital_query(client_query: ClientQuery, hospital: Hospital) -> None:
    response = client_query(
        f"""
       {{
           hospital(id: {hospital.id})  {{
                id
                name
            }}
        }}
        """
    )
    content = json.loads(response.content)
    assert "errors" not in content

    data = content["data"]["hospital"]
    assert data["name"] == hospital.name


@pytest.mark.django_db
def test_hospitals_query(
    client_query: ClientQuery, hospitals: list[Hospital]
) -> None:
    response = client_query(
        """
         {
            hospitals {
             id
              name
            }
         }
        """
    )
    content = json.loads(response.content)
    assert "errors" not in content

    data = content["data"]["hospitals"]
    for data_hospital, hospital in zip(data, hospitals):
        assert data_hospital["name"] == hospital.name
