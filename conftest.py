from http.client import HTTPResponse
from typing import Any, Callable

import pytest
from django.test import Client
from graphene_django.utils.testing import graphql_query


@pytest.fixture
def client_query(client: Client) -> Callable[..., HTTPResponse]:
    def func(*args: Any, **kwargs: Any) -> HTTPResponse:
        return graphql_query(*args, **kwargs, client=client)

    return func
