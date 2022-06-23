from functools import partial
from typing import TYPE_CHECKING

import pytest
from django.contrib.auth import get_user_model
from graphene_django.utils.testing import graphql_query


if TYPE_CHECKING:
    from users.models import CustomUser as UserType

User = get_user_model()


@pytest.fixture
def user() -> "UserType":
    user_obj = User(username="foo", email="foo@bar.com")
    user_obj.set_password("bar12345678")
    return user_obj


@pytest.mark.django_db
def test_register(client_query: partial[graphql_query]) -> None:
    response = client_query(
        """
        mutation register(
            $username: String!,
            $email: String!,
            $password1: String!,
            $password2: String!
        ){
            register(
                username: $username,
                email: $email,
                password1: $password1,
                password2: $password2
            ) {
                success
                errors
                refreshToken
                token
            }
        }
        """,
        op_name="register",
        variables={
            "username": "foo123",
            "email": "example@email.com",
            "password1": "fakePassword123",
            "password2": "fakePassword123",
        },
    )

    content = response.json()
    data = content["data"]["register"]

    assert data["success"]
    assert data["token"]
    assert data["refreshToken"]
    assert data["errors"] is None


class TestTokenAuth:
    @pytest.fixture
    @pytest.mark.django_db
    def test_success(self, client_query: partial[graphql_query]) -> None:
        response = client_query(
            """
            mutation token_auth($username: String!, $password: String!){
                token_auth(username: $username, password: $password) {
                    success
                    errors
                    token
                    user {
                        id
                    }
                }
            }
            """,
            op_name="token_auth",
            variables={
                "username": "foo123",
                "password": "fakePassword123",
            },
        )
        content = response.json()
        data = content["data"]["register"]
        assert data["token"]
        assert "password" not in data

    @pytest.fixture
    @pytest.mark.django_db
    def test_fail(
        self, user: "UserType", client_query: partial[graphql_query]
    ) -> None:
        client_query(
            """
            mutation token_auth($username: String!, $password: String!){
                token_auth(username: $username, password: $password) {
                    success
                    errors
                    token
                    user {
                        id
                    }
                }
            }
            """,
            op_name="token_auth",
            variables={
                "username": "foofoo",
                "password": "bar",
            },
        )

        with pytest.raises(User.DoesNotExist):
            user.refresh_from_db()


@pytest.mark.django_db
def test_profile_creation(client_query: partial[graphql_query]) -> None:
    user = User.objects.create_user(
        email="foo@spam2.com", username="foospam2", password="adminadmin"
    )

    response = client_query(
        """
        mutation login(
            $password: String!,
            $username: String,
            ) {
                login(
                    password: $password,
                    username: $username,
                ) {
                    token
                    success
                    errors
                    user{
                        id
                        profile{
                            id
                            cryptoWallet
                            phone
                        }
                    }
                }
            }
        """,
        op_name="login",
        variables=dict(username=user.username, password="adminadmin"),
    )

    content = response.json()
    user_data = content["data"]["login"]["user"]

    assert "profile" in user_data
