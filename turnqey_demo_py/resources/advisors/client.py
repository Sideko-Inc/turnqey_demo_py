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


class AdvisorsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AdvisorsListResponse:
        """
        Get financial advisors

        Retrieve a list of financial advisors

        GET /advisors

        Args:
            limit: Number of items per page
            page: Page number for pagination
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.advisors.list()
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
            path="/advisors",
            auth_names=["clientCredentials"],
            query_params=_query,
            cast_to=models.AdvisorsListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        advisor_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Advisor:
        """
        Get advisor by ID

        Retrieve a specific financial advisor by ID

        GET /advisors/{advisorId}

        Args:
            advisorId: ID of the advisor to retrieve
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.advisors.get(advisor_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/advisors/{advisor_id}",
            auth_names=["clientCredentials"],
            cast_to=models.Advisor,
            request_options=request_options or default_request_options(),
        )


class AsyncAdvisorsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AdvisorsListResponse:
        """
        Get financial advisors

        Retrieve a list of financial advisors

        GET /advisors

        Args:
            limit: Number of items per page
            page: Page number for pagination
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.advisors.list()
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
            path="/advisors",
            auth_names=["clientCredentials"],
            query_params=_query,
            cast_to=models.AdvisorsListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        advisor_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Advisor:
        """
        Get advisor by ID

        Retrieve a specific financial advisor by ID

        GET /advisors/{advisorId}

        Args:
            advisorId: ID of the advisor to retrieve
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.advisors.get(advisor_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/advisors/{advisor_id}",
            auth_names=["clientCredentials"],
            cast_to=models.Advisor,
            request_options=request_options or default_request_options(),
        )
