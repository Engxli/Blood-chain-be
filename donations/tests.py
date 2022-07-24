import json

import pytest
from django.contrib.auth import get_user_model
from graphql_jwt.shortcuts import get_token

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
def blood_request(user1: CustomUser) -> Request:
    user1_profile = UserProfile.objects.get(user=user1)
    return Request.objects.create(
        owner=user1_profile,
        blood_type=Request.BloodType.Amin,
        severity=Request.Severity.LOW,
        quantity=1000,
        file_number=1234,
        details="Gimme your blood",
    )


@pytest.mark.django_db
def test_donation_query(
    client_query: ClientQuery,
    blood_request: Request,
    user2: CustomUser,
) -> None:

    user2_profile = UserProfile.objects.get(user=user2)

    Donation.objects.create(
        status=Donation.Status.COMPLETE,
        request=blood_request,
        donor=user2_profile,
    )

    Donation.objects.create(
        status=Donation.Status.PENDING,
        request=blood_request,
        donor=user2_profile,
    )

    Donation.objects.create(
        status=Donation.Status.COMPLETE,
        request=blood_request,
        donor=user2_profile,
    )

    Donation.objects.create(
        status=Donation.Status.COMPLETE,
        request=blood_request,
        donor=user2_profile,
    )

    token = get_token(user2)
    headers = {"HTTP_AUTHORIZATION": f"JWT {token}"}

    response = client_query(
        """
        query{
            user-donations{
                id
                donor{
                    user{
                        id
                        username
                    }
                }
            }
            }
        """,
        headers=headers,
    )

    content = json.loads(response.content)
    donations = content["data"]["user-donations"]

    assert "errors" not in content

    for donation in donations:
        donor_user_id = donation["donor"]["user"]["id"]
        assert donor_user_id == str(user2.id)


@pytest.mark.django_db
def test_pending_donation_query(
    client_query: ClientQuery,
    blood_request: Request,
    user2: CustomUser,
) -> None:

    user2_profile = UserProfile.objects.get(user=user2)

    Donation.objects.create(
        status=Donation.Status.COMPLETE,
        request=blood_request,
        donor=user2_profile,
    )
    Donation.objects.create(
        status=Donation.Status.PENDING,
        request=blood_request,
        donor=user2_profile,
    )
    Donation.objects.create(
        status=Donation.Status.PENDING,
        request=blood_request,
        donor=user2_profile,
    )
    Donation.objects.create(
        status=Donation.Status.CANCELED,
        request=blood_request,
        donor=user2_profile,
    )

    token = get_token(user2)
    headers = {"HTTP_AUTHORIZATION": f"JWT {token}"}

    response = client_query(
        """
        query user-donations($pending: Boolean){
            userDonations(pending: $pending) {
                id
                status
                donor{
                    user{
                        id
                        username
                    }
                }
            }
            }
        """,
        headers=headers,
        variables=dict(pending=True),
    )

    content = json.loads(response.content)
    assert "errors" not in content

    donations = content["data"]["user-donations"]

    for donation in donations:
        status = donation["status"]
        donor_user_id = donation["donor"]["user"]["id"]

        assert donor_user_id == str(user2.id)
        assert status == Donation.Status.PENDING
