import httpx
import typing

from turnqey_demo_py.core import (
    AsyncBaseClient,
    AuthBearer,
    GrantType,
    OAuth2,
    OAuth2ClientCredentialsForm,
    SyncBaseClient,
)
from turnqey_demo_py.environment import Environment
from turnqey_demo_py.resources.advisors import AdvisorsClient, AsyncAdvisorsClient
from turnqey_demo_py.resources.auth import AsyncAuthClient, AuthClient
from turnqey_demo_py.resources.clients import AsyncClientsClient, ClientsClient
from turnqey_demo_py.resources.prices import AsyncPricesClient, PricesClient


class Client:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None,
        environment: Environment = Environment.PRODUCTION,
        token: typing.Optional[OAuth2ClientCredentialsForm] = None,
    ):
        """Initialize root client"""
        self._base_client = SyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=httpx.Client(timeout=timeout)
            if httpx_client is None
            else httpx_client,
        )
        self._base_client.register_auth(
            "clientCredentials",
            OAuth2(
                token_url=self._base_client.build_url("/NewAccessToken"),
                access_token_pointer="/access_token",
                expires_in_pointer="/expires_in",
                credentials_location="request_body",
                body_content="json",
                grant_type=typing.cast(
                    GrantType,
                    token.get("grant_type", "client_credentials")
                    if token
                    else "client_credentials",
                ),
                client_id=None if not token else token.get("client_id"),
                client_secret=None if not token else token.get("client_secret"),
                scope=None if not token else token.get("scope"),
                request_mutator=AuthBearer(val=None),
            ),
        )
        self.clients = ClientsClient(base_client=self._base_client)
        self.advisors = AdvisorsClient(base_client=self._base_client)
        self.prices = PricesClient(base_client=self._base_client)
        self.auth = AuthClient(base_client=self._base_client)


class AsyncClient:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        environment: Environment = Environment.PRODUCTION,
        token: typing.Optional[OAuth2ClientCredentialsForm] = None,
    ):
        """Initialize root client"""
        self._base_client = AsyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=httpx.AsyncClient(timeout=timeout)
            if httpx_client is None
            else httpx_client,
        )
        self._base_client.register_auth(
            "clientCredentials",
            OAuth2(
                token_url=self._base_client.build_url("/NewAccessToken"),
                access_token_pointer="/access_token",
                expires_in_pointer="/expires_in",
                credentials_location="request_body",
                body_content="json",
                grant_type=typing.cast(
                    GrantType,
                    token.get("grant_type", "client_credentials")
                    if token
                    else "client_credentials",
                ),
                client_id=None if not token else token.get("client_id"),
                client_secret=None if not token else token.get("client_secret"),
                scope=None if not token else token.get("scope"),
                request_mutator=AuthBearer(val=None),
            ),
        )
        self.clients = AsyncClientsClient(base_client=self._base_client)
        self.advisors = AsyncAdvisorsClient(base_client=self._base_client)
        self.prices = AsyncPricesClient(base_client=self._base_client)
        self.auth = AsyncAuthClient(base_client=self._base_client)


def _get_base_url(
    *, base_url: typing.Optional[str] = None, environment: Environment
) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Must include a base_url or environment arguments")
