import pydantic
import typing

from .balance_exchange_balances_item import BalanceExchangeBalancesItem
from .balance_wallet_balances_item import BalanceWalletBalancesItem


class Balance(pydantic.BaseModel):
    """
    Balance
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    asset: typing.Optional[str] = pydantic.Field(alias="asset", default=None)
    """
    Asset symbol
    """
    client_id: typing.Optional[str] = pydantic.Field(alias="client_id", default=None)
    """
    ID of the client
    """
    exchange_balances: typing.Optional[typing.List[BalanceExchangeBalancesItem]] = (
        pydantic.Field(alias="exchange_balances", default=None)
    )
    quantity: typing.Optional[float] = pydantic.Field(alias="quantity", default=None)
    """
    Total quantity of the asset
    """
    updated_at: typing.Optional[str] = pydantic.Field(alias="updated_at", default=None)
    """
    When the balance was last updated
    """
    usd_value: typing.Optional[float] = pydantic.Field(alias="usd_value", default=None)
    """
    Value in USD based on current price
    """
    wallet_balances: typing.Optional[typing.List[BalanceWalletBalancesItem]] = (
        pydantic.Field(alias="wallet_balances", default=None)
    )
