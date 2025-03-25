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
from turnqey_demo_py.resources.clients.balances import (
    AsyncBalancesClient,
    BalancesClient,
)
from turnqey_demo_py.resources.clients.costbasis import (
    AsyncCostbasisClient,
    CostbasisClient,
)
from turnqey_demo_py.resources.clients.deposits_withdrawals import (
    AsyncDepositsWithdrawalsClient,
    DepositsWithdrawalsClient,
)
from turnqey_demo_py.resources.clients.exchanges import (
    AsyncExchangesClient,
    ExchangesClient,
)
from turnqey_demo_py.resources.clients.total_deposits_withdrawals import (
    AsyncTotalDepositsWithdrawalsClient,
    TotalDepositsWithdrawalsClient,
)
from turnqey_demo_py.resources.clients.trades import AsyncTradesClient, TradesClient
from turnqey_demo_py.resources.clients.transactions import (
    AsyncTransactionsClient,
    TransactionsClient,
)
from turnqey_demo_py.resources.clients.transfers import (
    AsyncTransfersClient,
    TransfersClient,
)
from turnqey_demo_py.resources.clients.wallets import AsyncWalletsClient, WalletsClient
from turnqey_demo_py.types import models, params


class ClientsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.wallets = WalletsClient(base_client=self._base_client)
        self.balances = BalancesClient(base_client=self._base_client)
        self.costbasis = CostbasisClient(base_client=self._base_client)
        self.deposits_withdrawals = DepositsWithdrawalsClient(
            base_client=self._base_client
        )
        self.exchanges = ExchangesClient(base_client=self._base_client)
        self.total_deposits_withdrawals = TotalDepositsWithdrawalsClient(
            base_client=self._base_client
        )
        self.trades = TradesClient(base_client=self._base_client)
        self.transactions = TransactionsClient(base_client=self._base_client)
        self.transfers = TransfersClient(base_client=self._base_client)

    def delete(
        self, *, client_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete client

        Delete a client by ID

        DELETE /clients/{clientId}

        Args:
            clientId: ID of the client
            request_options: Additional options to customize the HTTP request

        Returns:
            Client deleted successfully

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.clients.delete(client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/clients/{client_id}",
            auth_names=["clientCredentials"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

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
    ) -> models.ClientsListResponse:
        """
        Get all clients

        Retrieve a list of all clients

        GET /clients

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
        client.clients.list()
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
            path="/clients",
            auth_names=["clientCredentials"],
            query_params=_query,
            cast_to=models.ClientsListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self, *, client_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Client:
        """
        Get client by ID

        Retrieve a specific client by ID

        GET /clients/{clientId}

        Args:
            clientId: ID of the client
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.clients.get(client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/clients/{client_id}",
            auth_names=["clientCredentials"],
            cast_to=models.Client,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        email_field: str,
        name: str,
        phone: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Client:
        """
        Create a new client

        Create a new client in the system

        POST /clients

        Args:
            phone: Phone number of the client
            email: Email address of the client
            name: Full name of the client
            request_options: Additional options to customize the HTTP request

        Returns:
            Client created successfully

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.clients.create(email_field="mail@example.com", name="string")
        ```
        """
        _json = to_encodable(
            item={"phone": phone, "email_field": email_field, "name": name},
            dump_with=params._SerializerClientCreate,
        )
        return self._base_client.request(
            method="POST",
            path="/clients",
            auth_names=["clientCredentials"],
            json=_json,
            cast_to=models.Client,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        client_id: str,
        email_field: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        phone: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Client:
        """
        Update client

        Update an existing client

        PUT /clients/{clientId}

        Args:
            email: Email address of the client
            name: Full name of the client
            phone: Phone number of the client
            clientId: ID of the client
            request_options: Additional options to customize the HTTP request

        Returns:
            Client updated successfully

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.clients.update(client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
        ```
        """
        _json = to_encodable(
            item={"email_field": email_field, "name": name, "phone": phone},
            dump_with=params._SerializerClientUpdate,
        )
        return self._base_client.request(
            method="PUT",
            path=f"/clients/{client_id}",
            auth_names=["clientCredentials"],
            json=_json,
            cast_to=models.Client,
            request_options=request_options or default_request_options(),
        )


class AsyncClientsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.wallets = AsyncWalletsClient(base_client=self._base_client)
        self.balances = AsyncBalancesClient(base_client=self._base_client)
        self.costbasis = AsyncCostbasisClient(base_client=self._base_client)
        self.deposits_withdrawals = AsyncDepositsWithdrawalsClient(
            base_client=self._base_client
        )
        self.exchanges = AsyncExchangesClient(base_client=self._base_client)
        self.total_deposits_withdrawals = AsyncTotalDepositsWithdrawalsClient(
            base_client=self._base_client
        )
        self.trades = AsyncTradesClient(base_client=self._base_client)
        self.transactions = AsyncTransactionsClient(base_client=self._base_client)
        self.transfers = AsyncTransfersClient(base_client=self._base_client)

    async def delete(
        self, *, client_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete client

        Delete a client by ID

        DELETE /clients/{clientId}

        Args:
            clientId: ID of the client
            request_options: Additional options to customize the HTTP request

        Returns:
            Client deleted successfully

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.clients.delete(client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/clients/{client_id}",
            auth_names=["clientCredentials"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

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
    ) -> models.ClientsListResponse:
        """
        Get all clients

        Retrieve a list of all clients

        GET /clients

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
        await client.clients.list()
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
            path="/clients",
            auth_names=["clientCredentials"],
            query_params=_query,
            cast_to=models.ClientsListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self, *, client_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Client:
        """
        Get client by ID

        Retrieve a specific client by ID

        GET /clients/{clientId}

        Args:
            clientId: ID of the client
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.clients.get(client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/clients/{client_id}",
            auth_names=["clientCredentials"],
            cast_to=models.Client,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        email_field: str,
        name: str,
        phone: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Client:
        """
        Create a new client

        Create a new client in the system

        POST /clients

        Args:
            phone: Phone number of the client
            email: Email address of the client
            name: Full name of the client
            request_options: Additional options to customize the HTTP request

        Returns:
            Client created successfully

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.clients.create(email_field="mail@example.com", name="string")
        ```
        """
        _json = to_encodable(
            item={"phone": phone, "email_field": email_field, "name": name},
            dump_with=params._SerializerClientCreate,
        )
        return await self._base_client.request(
            method="POST",
            path="/clients",
            auth_names=["clientCredentials"],
            json=_json,
            cast_to=models.Client,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        client_id: str,
        email_field: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        phone: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Client:
        """
        Update client

        Update an existing client

        PUT /clients/{clientId}

        Args:
            email: Email address of the client
            name: Full name of the client
            phone: Phone number of the client
            clientId: ID of the client
            request_options: Additional options to customize the HTTP request

        Returns:
            Client updated successfully

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.clients.update(client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
        ```
        """
        _json = to_encodable(
            item={"email_field": email_field, "name": name, "phone": phone},
            dump_with=params._SerializerClientUpdate,
        )
        return await self._base_client.request(
            method="PUT",
            path=f"/clients/{client_id}",
            auth_names=["clientCredentials"],
            json=_json,
            cast_to=models.Client,
            request_options=request_options or default_request_options(),
        )
