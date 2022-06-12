from typing import Any

import pytest
from django.test import Client
from graphene_django.utils.testing import graphql_query


@pytest.fixture
def client_query(client: Client) -> Any:
    def func(*args: Any, **kwargs: Any) -> Any:
        return graphql_query(*args, **kwargs, client=client)

    return func
