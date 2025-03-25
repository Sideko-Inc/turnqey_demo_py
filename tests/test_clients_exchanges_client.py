import pydantic
import pytest

from turnqey_demo_py import AsyncClient, Client
from turnqey_demo_py.environment import Environment
from turnqey_demo_py.types import models


def test_create_201_success_default():
    """Tests a POST request to the /clients/{clientId}/exchanges endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.Exchange

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(
        token={"client_id": "OAUTH_CLIENT_ID", "client_secret": "OAUTH_CLIENT_SECRET"},
        environment=Environment.MOCK_SERVER,
    )
    response = client.clients.exchanges.create(
        api_key="abc123def456ghi789",
        api_secret="secret123456789",
        client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        exchange_name="Coinbase",
    )
    try:
        pydantic.TypeAdapter(models.Exchange).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_default():
    """Tests a POST request to the /clients/{clientId}/exchanges endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.Exchange

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(
        token={"client_id": "OAUTH_CLIENT_ID", "client_secret": "OAUTH_CLIENT_SECRET"},
        environment=Environment.MOCK_SERVER,
    )
    response = await client.clients.exchanges.create(
        api_key="abc123def456ghi789",
        api_secret="secret123456789",
        client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        exchange_name="Coinbase",
    )
    try:
        pydantic.TypeAdapter(models.Exchange).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /clients/{clientId}/exchanges endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ClientsExchangesGetResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(
        token={"client_id": "OAUTH_CLIENT_ID", "client_secret": "OAUTH_CLIENT_SECRET"},
        environment=Environment.MOCK_SERVER,
    )
    response = client.clients.exchanges.get(
        client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    try:
        pydantic.TypeAdapter(models.ClientsExchangesGetResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /clients/{clientId}/exchanges endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ClientsExchangesGetResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(
        token={"client_id": "OAUTH_CLIENT_ID", "client_secret": "OAUTH_CLIENT_SECRET"},
        environment=Environment.MOCK_SERVER,
    )
    response = await client.clients.exchanges.get(
        client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    try:
        pydantic.TypeAdapter(models.ClientsExchangesGetResponse).validate_python(
            response
        )
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
