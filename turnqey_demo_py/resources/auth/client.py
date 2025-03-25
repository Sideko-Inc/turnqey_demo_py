import typing

from turnqey_demo_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
)
from turnqey_demo_py.types import models, params


class AuthClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create_token(
        self,
        *,
        client_id: str,
        client_secret: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TokenResponse:
        """
        Generate access token using client ID and client secret

        Authenticates with the provided credentials and returns an access token

        POST /auth/token

        Args:
            client_id: Client ID provided by Turnqey
            client_secret: Client secret provided by Turnqey
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful authentication

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.auth.create_token(client_id="string", client_secret="string")
        ```
        """
        _json = to_encodable(
            item={"client_id": client_id, "client_secret": client_secret},
            dump_with=params._SerializerTokenRequest,
        )
        return self._base_client.request(
            method="POST",
            path="/NewAccessToken",
            json=_json,
            cast_to=models.TokenResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAuthClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create_token(
        self,
        *,
        client_id: str,
        client_secret: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TokenResponse:
        """
        Generate access token using client ID and client secret

        Authenticates with the provided credentials and returns an access token

        POST /auth/token

        Args:
            client_id: Client ID provided by Turnqey
            client_secret: Client secret provided by Turnqey
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful authentication

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.auth.create_token(client_id="string", client_secret="string")
        ```
        """
        _json = to_encodable(
            item={"client_id": client_id, "client_secret": client_secret},
            dump_with=params._SerializerTokenRequest,
        )
        return await self._base_client.request(
            method="POST",
            path="/NewAccessToken",
            json=_json,
            cast_to=models.TokenResponse,
            request_options=request_options or default_request_options(),
        )
