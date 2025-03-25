import pydantic
import typing


class BalanceExchangeBalancesItem(pydantic.BaseModel):
    """
    BalanceExchangeBalancesItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    exchange_id: typing.Optional[str] = pydantic.Field(
        alias="exchange_id", default=None
    )
    """
    ID of the exchange
    """
    quantity: typing.Optional[float] = pydantic.Field(alias="quantity", default=None)
    """
    Quantity in this exchange
    """
