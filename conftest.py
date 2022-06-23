from typing import Any, Protocol

import pytest
from django.test import Client
from graphene_django.utils.testing import graphql_query


class ClientQuery(Protocol):
    def __call__(
        self,
        query: Any,
        op_name: Any = ...,
        input_data: Any = ...,
        variables: Any = ...,
        headers: Any = ...,
        graphql_url: Any = ...,
    ) -> Any:
        ...


@pytest.fixture
def client_query(client: Client) -> ClientQuery:
    def _client_query(*args: Any, **kwargs: Any) -> Any:
        return graphql_query(*args, **kwargs, client=client)

    return _client_query
