import pydantic
import pytest

from turnqey_demo_py import AsyncClient, Client
from turnqey_demo_py.environment import Environment
from turnqey_demo_py.types import models


def test_get_200_generated_success():
    """Tests a GET request to the /clients/{clientId}/total-deposits-withdrawals endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TotalDepositWithdrawal

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
    response = client.clients.total_deposits_withdrawals.get(
        client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    try:
        pydantic.TypeAdapter(models.TotalDepositWithdrawal).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /clients/{clientId}/total-deposits-withdrawals endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TotalDepositWithdrawal

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
    response = await client.clients.total_deposits_withdrawals.get(
        client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    try:
        pydantic.TypeAdapter(models.TotalDepositWithdrawal).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
