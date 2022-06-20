from functools import partial

import pytest
from django.test import Client
from graphene_django.utils.testing import graphql_query


@pytest.fixture
def client_query(client: Client) -> partial[graphql_query]:
    return partial(graphql_query, client=client)
