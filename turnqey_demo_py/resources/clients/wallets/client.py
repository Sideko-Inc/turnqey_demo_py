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


class WalletsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        client_id: str,
        wallet_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Remove wallet

        Remove a wallet from a client

        DELETE /clients/{clientId}/wallets/{walletId}

        Args:
            clientId: ID of the client
            walletId: ID of the wallet to remove
            request_options: Additional options to customize the HTTP request

        Returns:
            Wallet removed successfully

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.clients.wallets.delete(
            client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", wallet_id="string"
        )
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/clients/{client_id}/wallets/{wallet_id}",
            auth_names=["clientCredentials"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def list(
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
    ) -> models.ClientsWalletsListResponse:
        """
        Get client wallets

        Retrieve a list of wallets for a specific client

        GET /clients/{clientId}/wallets

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
        client.clients.wallets.list(client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
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
            path=f"/clients/{client_id}/wallets",
            auth_names=["clientCredentials"],
            query_params=_query,
            cast_to=models.ClientsWalletsListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        client_id: str,
        wallet_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Wallet:
        """
        Get specific wallet

        Retrieve a specific wallet for a client

        GET /clients/{clientId}/wallets/{walletId}

        Args:
            clientId: ID of the client
            walletId: ID of the wallet to retrieve
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.clients.wallets.get(
            client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", wallet_id="string"
        )
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/clients/{client_id}/wallets/{wallet_id}",
            auth_names=["clientCredentials"],
            cast_to=models.Wallet,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        address: str,
        blockchain: str,
        client_id: str,
        label: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Wallet:
        """
        Add wallet to client

        Add a new wallet for a specific client

        POST /clients/{clientId}/wallets

        Args:
            label: User-defined label for the wallet
            address: Blockchain address of the wallet
            blockchain: Blockchain network (e.g. Ethereum, Bitcoin)
            clientId: ID of the client
            request_options: Additional options to customize the HTTP request

        Returns:
            Wallet added successfully

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.clients.wallets.create(
            address="string",
            blockchain="string",
            client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```
        """
        _json = to_encodable(
            item={"label": label, "address": address, "blockchain": blockchain},
            dump_with=params._SerializerWalletCreate,
        )
        return self._base_client.request(
            method="POST",
            path=f"/clients/{client_id}/wallets",
            auth_names=["clientCredentials"],
            json=_json,
            cast_to=models.Wallet,
            request_options=request_options or default_request_options(),
        )


class AsyncWalletsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        client_id: str,
        wallet_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Remove wallet

        Remove a wallet from a client

        DELETE /clients/{clientId}/wallets/{walletId}

        Args:
            clientId: ID of the client
            walletId: ID of the wallet to remove
            request_options: Additional options to customize the HTTP request

        Returns:
            Wallet removed successfully

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.clients.wallets.delete(
            client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", wallet_id="string"
        )
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/clients/{client_id}/wallets/{wallet_id}",
            auth_names=["clientCredentials"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def list(
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
    ) -> models.ClientsWalletsListResponse:
        """
        Get client wallets

        Retrieve a list of wallets for a specific client

        GET /clients/{clientId}/wallets

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
        await client.clients.wallets.list(
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
            path=f"/clients/{client_id}/wallets",
            auth_names=["clientCredentials"],
            query_params=_query,
            cast_to=models.ClientsWalletsListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        client_id: str,
        wallet_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Wallet:
        """
        Get specific wallet

        Retrieve a specific wallet for a client

        GET /clients/{clientId}/wallets/{walletId}

        Args:
            clientId: ID of the client
            walletId: ID of the wallet to retrieve
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.clients.wallets.get(
            client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", wallet_id="string"
        )
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/clients/{client_id}/wallets/{wallet_id}",
            auth_names=["clientCredentials"],
            cast_to=models.Wallet,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        address: str,
        blockchain: str,
        client_id: str,
        label: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Wallet:
        """
        Add wallet to client

        Add a new wallet for a specific client

        POST /clients/{clientId}/wallets

        Args:
            label: User-defined label for the wallet
            address: Blockchain address of the wallet
            blockchain: Blockchain network (e.g. Ethereum, Bitcoin)
            clientId: ID of the client
            request_options: Additional options to customize the HTTP request

        Returns:
            Wallet added successfully

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.clients.wallets.create(
            address="string",
            blockchain="string",
            client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        )
        ```
        """
        _json = to_encodable(
            item={"label": label, "address": address, "blockchain": blockchain},
            dump_with=params._SerializerWalletCreate,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/clients/{client_id}/wallets",
            auth_names=["clientCredentials"],
            json=_json,
            cast_to=models.Wallet,
            request_options=request_options or default_request_options(),
        )
