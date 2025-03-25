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
from turnqey_demo_py.types import models


class TotalDepositsWithdrawalsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self,
        *,
        client_id: str,
        date_from: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        date_to: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TotalDepositWithdrawal:
        """
        Get client total deposits and withdrawals

        Retrieve total deposits and withdrawals for a client

        GET /clients/{clientId}/total-deposits-withdrawals

        Args:
            dateFrom: Start date for filtering (YYYY-MM-DD)
            dateTo: End date for filtering (YYYY-MM-DD)
            clientId: ID of the client
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.clients.total_deposits_withdrawals.get(
            client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(date_from, type_utils.NotGiven):
            encode_query_param(
                _query,
                "dateFrom",
                to_encodable(item=date_from, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(date_to, type_utils.NotGiven):
            encode_query_param(
                _query,
                "dateTo",
                to_encodable(item=date_to, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path=f"/clients/{client_id}/total-deposits-withdrawals",
            auth_names=["clientCredentials"],
            query_params=_query,
            cast_to=models.TotalDepositWithdrawal,
            request_options=request_options or default_request_options(),
        )


class AsyncTotalDepositsWithdrawalsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self,
        *,
        client_id: str,
        date_from: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        date_to: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TotalDepositWithdrawal:
        """
        Get client total deposits and withdrawals

        Retrieve total deposits and withdrawals for a client

        GET /clients/{clientId}/total-deposits-withdrawals

        Args:
            dateFrom: Start date for filtering (YYYY-MM-DD)
            dateTo: End date for filtering (YYYY-MM-DD)
            clientId: ID of the client
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.clients.total_deposits_withdrawals.get(
            client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(date_from, type_utils.NotGiven):
            encode_query_param(
                _query,
                "dateFrom",
                to_encodable(item=date_from, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(date_to, type_utils.NotGiven):
            encode_query_param(
                _query,
                "dateTo",
                to_encodable(item=date_to, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path=f"/clients/{client_id}/total-deposits-withdrawals",
            auth_names=["clientCredentials"],
            query_params=_query,
            cast_to=models.TotalDepositWithdrawal,
            request_options=request_options or default_request_options(),
        )
