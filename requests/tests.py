import json

import pytest
from django.contrib.auth import get_user_model

from conftest import ClientQuery
from requests.models import Request


@pytest.fixture
@pytest.mark.django_db
def request_() -> Request:
    User = get_user_model()
    user1 = User.objects.create(username="user1", password="ILoveDjango!")
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
    blood_type = {
        "A+": "A__1",
        "A-": "A_",
        "B+": "B__3",
        "B-": "B_",
        "O+": "O__5",
        "O-": "O_",
        "AB+": "AB__7",
        "AB-": "AB_",
    }
    response = client_query(
        f"""
        query{{
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
    assert data["bloodType"] in blood_type[request_.blood_type]
    assert data["severity"] in request_.severity
    assert data["quantity"] == request_.quantity
    assert data["details"] in request_.details


@pytest.fixture
@pytest.mark.django_db
def requests() -> list[Request]:
    User = get_user_model()
    user1 = User.objects.create(username="admin1", password="ILoveDjango!")
    user2 = User.objects.create(username="admin2", password="ILoveDjango!")
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
    blood_type = {
        "A+": "A__1",
        "A-": "A_",
        "B+": "B__3",
        "B-": "B_",
        "O+": "O__5",
        "O-": "O_",
        "AB+": "AB__7",
        "AB-": "AB_",
    }
    response = client_query(
        """
        query{
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
    data = content["data"]["requests"]
    for request, data_request in zip(requests, data):
        assert data_request["owner"]["id"] == str(request.owner.id)
        assert data_request["bloodType"] in blood_type[request.blood_type]
        assert data_request["severity"] in request.severity
        assert data_request["quantity"] == request.quantity
        assert data_request["details"] in request.details


@pytest.mark.django_db
def test_requests_query_eligible_true_not_logged_in(
    client_query: ClientQuery, requests: list[Request]
) -> None:
    response = client_query(
        """
        query{
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
