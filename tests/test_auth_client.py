import pydantic
import pytest

from turnqey_demo_py import AsyncClient, Client
from turnqey_demo_py.environment import Environment
from turnqey_demo_py.types import models


def test_create_token_200_success_default():
    """Tests a POST request to the /auth/token endpoint.

    Operation: create_token
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TokenResponse

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
    response = client.auth.create_token(
        client_id="c3f42b1a-1e4d-4b8f-9c5e-7d6a3b2c1e4f",
        client_secret="d7e8f9a0-b1c2-3d4e-5f6a-7b8c9d0e1f2a",
    )
    try:
        pydantic.TypeAdapter(models.TokenResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_token_200_success_default():
    """Tests a POST request to the /auth/token endpoint.

    Operation: create_token
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TokenResponse

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
    response = await client.auth.create_token(
        client_id="c3f42b1a-1e4d-4b8f-9c5e-7d6a3b2c1e4f",
        client_secret="d7e8f9a0-b1c2-3d4e-5f6a-7b8c9d0e1f2a",
    )
    try:
        pydantic.TypeAdapter(models.TokenResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
