import pydantic
import typing


class BalanceWalletBalancesItem(pydantic.BaseModel):
    """
    BalanceWalletBalancesItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    quantity: typing.Optional[float] = pydantic.Field(alias="quantity", default=None)
    """
    Quantity in this wallet
    """
    wallet_id: typing.Optional[str] = pydantic.Field(alias="wallet_id", default=None)
    """
    ID of the wallet
    """
