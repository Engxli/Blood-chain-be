from functools import partial

import pytest
from django.contrib.auth import get_user_model
from graphene_django.utils.testing import graphql_query


User = get_user_model()


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
