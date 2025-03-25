import pydantic
import pytest

from turnqey_demo_py import AsyncClient, Client
from turnqey_demo_py.environment import Environment
from turnqey_demo_py.types import models


def test_update_200_success_default():
    """Tests a PUT request to the /clients/{clientId} endpoint.

    Operation: update
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Client

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
    response = client.clients.update(
        client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        email_field="john.doe@example.com",
        name="John Doe",
        phone="+1-555-123-4567",
    )
    try:
        pydantic.TypeAdapter(models.Client).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_200_success_default():
    """Tests a PUT request to the /clients/{clientId} endpoint.

    Operation: update
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Client

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
    response = await client.clients.update(
        client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        email_field="john.doe@example.com",
        name="John Doe",
        phone="+1-555-123-4567",
    )
    try:
        pydantic.TypeAdapter(models.Client).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_create_201_success_default():
    """Tests a POST request to the /clients endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.Client

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
    response = client.clients.create(
        email_field="john.doe@example.com", name="John Doe", phone="+1-555-123-4567"
    )
    try:
        pydantic.TypeAdapter(models.Client).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_default():
    """Tests a POST request to the /clients endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.Client

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
    response = await client.clients.create(
        email_field="john.doe@example.com", name="John Doe", phone="+1-555-123-4567"
    )
    try:
        pydantic.TypeAdapter(models.Client).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /clients/{clientId} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Client

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
    response = client.clients.get(client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
    try:
        pydantic.TypeAdapter(models.Client).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /clients/{clientId} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Client

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
    response = await client.clients.get(
        client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    try:
        pydantic.TypeAdapter(models.Client).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_list_200_generated_success():
    """Tests a GET request to the /clients endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ClientsListResponse

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
    response = client.clients.list()
    try:
        pydantic.TypeAdapter(models.ClientsListResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /clients endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ClientsListResponse

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
    response = await client.clients.list()
    try:
        pydantic.TypeAdapter(models.ClientsListResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_delete_204_generated_success():
    """Tests a DELETE request to the /clients/{clientId} endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 204
    Mode: Synchronous execution

    Empty response expected

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
    response = client.clients.delete(client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
    assert response is None


@pytest.mark.asyncio
async def test_await_delete_204_generated_success():
    """Tests a DELETE request to the /clients/{clientId} endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 204
    Mode: Asynchronous execution

    Empty response expected

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
    response = await client.clients.delete(
        client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    assert response is None
