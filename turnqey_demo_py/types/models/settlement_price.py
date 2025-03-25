import pydantic
import typing


class SettlementPrice(pydantic.BaseModel):
    """
    SettlementPrice
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    date: typing.Optional[str] = pydantic.Field(alias="date", default=None)
    """
    Settlement date
    """
    price: typing.Optional[float] = pydantic.Field(alias="price", default=None)
    """
    Settlement price in USD
    """
    source: typing.Optional[str] = pydantic.Field(alias="source", default=None)
    """
    Source of the settlement price
    """
    symbol_field: typing.Optional[str] = pydantic.Field(alias="symbol", default=None)
    """
    Asset symbol
    """
