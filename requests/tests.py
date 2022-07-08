import json

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from conftest import ClientQuery
from requests.models import Request
from users.models import CustomUser


User = get_user_model()


def create_user(username: str, password: str = "ILoveDjango!") -> CustomUser:
    return User.objects.create(
        username=username, password=make_password(password)
    )


@pytest.fixture
@pytest.mark.django_db
def request_() -> Request:
    user1 = create_user(username="user1")
    request = Request.objects.create(
        owner=user1.profile,
        blood_type=Request.BloodType.Omin,
        severity=Request.Severity.HIGH,
        quantity=500,
        details="No details yet!",
    )
    return request


@pytest.mark.django_db
def test_request_query(client_query: ClientQuery, request_: Request) -> None:
    response = client_query(
        f"""
        query {{
            request(id: {request_.id}) {{
                id
                owner {{
                    id
                }}
                bloodType
                severity
                quantity
                details
            }}
        }}
        """
    )

    content = json.loads(response.content)
    assert "errors" not in content

    data = content["data"]["request"]
    assert data["owner"]["id"] == str(request_.owner.id)
    assert data["bloodType"] == Request.BloodType(request_.blood_type).name
    assert data["severity"] in request_.severity
    assert data["quantity"] == request_.quantity
    assert data["details"] in request_.details


@pytest.fixture
@pytest.mark.django_db
def requests() -> list[Request]:
    user1 = create_user(username="admin1")
    user2 = create_user(username="admin2")

    request1 = Request.objects.create(
        owner=user1.profile,
        blood_type=Request.BloodType.Omin,
        severity=Request.Severity.HIGH,
        quantity=500,
        details="No details yet!",
    )
    request2 = Request.objects.create(
        owner=user2.profile,
        blood_type=Request.BloodType.Omin,
        severity=Request.Severity.HIGH,
        quantity=500,
        details="No details yet!",
    )

    return [request1, request2]


@pytest.mark.django_db
def test_requests_query_eligible_false(
    client_query: ClientQuery, requests: list[Request]
) -> None:
    response = client_query(
        """
        query {
            requests(onlyEligible:false) {
                id
                owner {
                    id
                    bloodType
                }
                bloodType
                severity
                quantity
                details
            }
        }
        """
    )

    content = json.loads(response.content)
    assert "errors" not in content

    all_data = content["data"]["requests"]
    for request, data in zip(requests, all_data):
        assert data["owner"]["id"] == str(request.owner.id)
        assert data["bloodType"] == Request.BloodType(request.blood_type).name
        assert data["severity"] in request.severity
        assert data["quantity"] == request.quantity
        assert data["details"] in request.details


@pytest.mark.django_db
def test_requests_query_eligible_true_not_logged_in(
    client_query: ClientQuery,
) -> None:
    response = client_query(
        """
        query {
            requests(onlyEligible:true) {
                id
                owner {
                    id
                    bloodType
                }
                bloodType
                severity
                quantity
                details
            }
        }
        """
    )

    content = json.loads(response.content)
    assert "errors" in content
