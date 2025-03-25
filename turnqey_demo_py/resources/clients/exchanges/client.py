import typing

from turnqey_demo_py.core import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
    type_utils,
)
from turnqey_demo_py.types import models, params


class ExchangesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self,
        *,
        client_id: str,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ClientsExchangesGetResponse:
        """
        Get client exchanges

        Retrieve a list of exchanges for a specific client

        GET /clients/{clientId}/exchanges

        Args:
            limit: Number of items per page
            page: Page number for pagination
            clientId: ID of the client
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.clients.exchanges.get(client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(limit, type_utils.NotGiven):
            encode_query_param(
                _query,
                "limit",
                to_encodable(item=limit, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page",
                to_encodable(item=page, dump_with=int),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path=f"/clients/{client_id}/exchanges",
            auth_names=["clientCredentials"],
            query_params=_query,
            cast_to=models.ClientsExchangesGetResponse,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        api_key: str,
        api_secret: str,
        client_id: str,
        exchange_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Exchange:
        """
        Add exchange to client

        Add a new exchange for a specific client

        POST /clients/{clientId}/exchanges

        Args:
            api_key: API key for the exchange
            api_secret: API secret for the exchange
            clientId: ID of the client
            exchange_name: Name of the exchange
            request_options: Additional options to customize the HTTP request

        Returns:
            Exchange added successfully

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.clients.exchanges.create(
            api_key="string",
            api_secret="string",
            client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            exchange_name="string",
        )
        ```
        """
        _json = to_encodable(
            item={
                "api_key": api_key,
                "api_secret": api_secret,
                "exchange_name": exchange_name,
            },
            dump_with=params._SerializerExchangeCreate,
        )
        return self._base_client.request(
            method="POST",
            path=f"/clients/{client_id}/exchanges",
            auth_names=["clientCredentials"],
            json=_json,
            cast_to=models.Exchange,
            request_options=request_options or default_request_options(),
        )


class AsyncExchangesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self,
        *,
        client_id: str,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ClientsExchangesGetResponse:
        """
        Get client exchanges

        Retrieve a list of exchanges for a specific client

        GET /clients/{clientId}/exchanges

        Args:
            limit: Number of items per page
            page: Page number for pagination
            clientId: ID of the client
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.clients.exchanges.get(
            client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(limit, type_utils.NotGiven):
            encode_query_param(
                _query,
                "limit",
                to_encodable(item=limit, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page",
                to_encodable(item=page, dump_with=int),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path=f"/clients/{client_id}/exchanges",
            auth_names=["clientCredentials"],
            query_params=_query,
            cast_to=models.ClientsExchangesGetResponse,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        api_key: str,
        api_secret: str,
        client_id: str,
        exchange_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Exchange:
        """
        Add exchange to client

        Add a new exchange for a specific client

        POST /clients/{clientId}/exchanges

        Args:
            api_key: API key for the exchange
            api_secret: API secret for the exchange
            clientId: ID of the client
            exchange_name: Name of the exchange
            request_options: Additional options to customize the HTTP request

        Returns:
            Exchange added successfully

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.clients.exchanges.create(
            api_key="string",
            api_secret="string",
            client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            exchange_name="string",
        )
        ```
        """
        _json = to_encodable(
            item={
                "api_key": api_key,
                "api_secret": api_secret,
                "exchange_name": exchange_name,
            },
            dump_with=params._SerializerExchangeCreate,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/clients/{client_id}/exchanges",
            auth_names=["clientCredentials"],
            json=_json,
            cast_to=models.Exchange,
            request_options=request_options or default_request_options(),
        )
