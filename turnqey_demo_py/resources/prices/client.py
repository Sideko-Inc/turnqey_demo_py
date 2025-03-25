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
from turnqey_demo_py.resources.prices.holding import AsyncHoldingClient, HoldingClient
from turnqey_demo_py.resources.prices.settlement import (
    AsyncSettlementClient,
    SettlementClient,
)
from turnqey_demo_py.types import models


class PricesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.holding = HoldingClient(base_client=self._base_client)
        self.settlement = SettlementClient(base_client=self._base_client)

    def get(
        self,
        *,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        symbol_field: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PricesGetResponse:
        """
        Get current prices

        Retrieve current prices for assets

        GET /prices

        Args:
            limit: Number of items per page
            page: Page number for pagination
            symbol: Symbol of the asset
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.prices.get()
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
        if not isinstance(symbol_field, type_utils.NotGiven):
            encode_query_param(
                _query,
                "symbol",
                to_encodable(item=symbol_field, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/prices",
            auth_names=["clientCredentials"],
            query_params=_query,
            cast_to=models.PricesGetResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncPricesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.holding = AsyncHoldingClient(base_client=self._base_client)
        self.settlement = AsyncSettlementClient(base_client=self._base_client)

    async def get(
        self,
        *,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        symbol_field: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PricesGetResponse:
        """
        Get current prices

        Retrieve current prices for assets

        GET /prices

        Args:
            limit: Number of items per page
            page: Page number for pagination
            symbol: Symbol of the asset
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.prices.get()
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
        if not isinstance(symbol_field, type_utils.NotGiven):
            encode_query_param(
                _query,
                "symbol",
                to_encodable(item=symbol_field, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/prices",
            auth_names=["clientCredentials"],
            query_params=_query,
            cast_to=models.PricesGetResponse,
            request_options=request_options or default_request_options(),
        )
