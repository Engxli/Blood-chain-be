import json
from functools import partial

import pytest
from graphene_django.utils.testing import graphql_query

from hospitals.models import Hospital


@pytest.fixture
def hospital() -> Hospital:
    return Hospital.objects.create(name="foo")


@pytest.mark.django_db
def test_hospital_query(
    client_query: partial[graphql_query], hospital: Hospital
) -> None:
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
    # assert data["request"] == hospital.request
