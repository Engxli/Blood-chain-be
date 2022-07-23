import json

import pytest
from django.contrib.auth import get_user_model

from blood_requests.models import Request
from conftest import ClientQuery
from donations.models import Donation
from users.models import CustomUser, UserProfile


User = get_user_model()


@pytest.fixture
def user1() -> CustomUser:
    return User.objects.create(username="luis", password="adminadmin")


@pytest.fixture
def user2() -> CustomUser:
    return User.objects.create(username="malthunayan", password="adminadmin")


@pytest.fixture
def user3() -> CustomUser:
    return User.objects.create(username="ali", password="adminadmin")


@pytest.fixture
@pytest.mark.django_db
def requests(user1: CustomUser, user2: CustomUser) -> list[Request]:
    user1_profile = UserProfile.objects.get(user=user1)
    user2_profile = UserProfile.objects.get(user=user2)

    request1 = Request.objects.create(
        owner=user1_profile,
        blood_type=Request.BloodType.Omin,
        severity=Request.Severity.HIGH,
        quantity=500,
        file_number=1234,
        details="No details yet!",
    )
    request2 = Request.objects.create(
        owner=user2_profile,
        blood_type=Request.BloodType.Omin,
        severity=Request.Severity.HIGH,
        quantity=500,
        file_number=1234,
        details="No details yet!",
    )

    return [request1, request2]


@pytest.fixture
@pytest.mark.django_db
def donations(requests: list[Request], user3: CustomUser) -> list[Donation]:
    user3_profile = UserProfile.objects.get(user=user3)

    blood_request = requests[0]

    donation1 = Donation.objects.create(
        status=Donation.Status.COMPLETE,
        request=blood_request,
        donor=user3_profile,
    )

    return [donation1]


@pytest.mark.django_db
def test_analytics_query(
    client_query: ClientQuery,
    requests: list[Request],
    donations: list[Donation],
) -> None:
    response = client_query(
        """
        query {
            analytics {
                totalRequests
                totalDonations
                totalCases
            }
        }
        """
    )

    content = json.loads(response.content)
    total_requests = content["data"]["analytics"]["totalRequests"]
    total_donations = content["data"]["analytics"]["totalDonations"]
    total_cases = content["data"]["analytics"]["totalCases"]

    assert "errors" not in content
    assert total_requests == len(requests)
    assert total_donations == len(donations)
    assert total_cases == len(requests) + len(donations)
