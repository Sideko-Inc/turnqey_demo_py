import typing

from turnqey_demo_py.core import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
)
from turnqey_demo_py.types import models


class SettlementClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self,
        *,
        date: str,
        symbol_field: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SettlementPrice:
        """
        Get settlement price

        Retrieve settlement price for an asset

        GET /settlement-price

        Args:
            date: Date for the settlement price
            symbol: Symbol of the asset
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.prices.settlement.get(date="1970-01-01", symbol_field="string")
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "date",
            to_encodable(item=date, dump_with=str),
            style="form",
            explode=True,
        )
        encode_query_param(
            _query,
            "symbol",
            to_encodable(item=symbol_field, dump_with=str),
            style="form",
            explode=True,
        )
        return self._base_client.request(
            method="GET",
            path="/settlement-price",
            auth_names=["clientCredentials"],
            query_params=_query,
            cast_to=models.SettlementPrice,
            request_options=request_options or default_request_options(),
        )


class AsyncSettlementClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self,
        *,
        date: str,
        symbol_field: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SettlementPrice:
        """
        Get settlement price

        Retrieve settlement price for an asset

        GET /settlement-price

        Args:
            date: Date for the settlement price
            symbol: Symbol of the asset
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.prices.settlement.get(date="1970-01-01", symbol_field="string")
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "date",
            to_encodable(item=date, dump_with=str),
            style="form",
            explode=True,
        )
        encode_query_param(
            _query,
            "symbol",
            to_encodable(item=symbol_field, dump_with=str),
            style="form",
            explode=True,
        )
        return await self._base_client.request(
            method="GET",
            path="/settlement-price",
            auth_names=["clientCredentials"],
            query_params=_query,
            cast_to=models.SettlementPrice,
            request_options=request_options or default_request_options(),
        )
