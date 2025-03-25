import pydantic
import typing


class Price(pydantic.BaseModel):
    """
    Price
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    percent_change_24h: typing.Optional[float] = pydantic.Field(
        alias="percent_change_24h", default=None
    )
    """
    24-hour percent change
    """
    percent_change_7d: typing.Optional[float] = pydantic.Field(
        alias="percent_change_7d", default=None
    )
    """
    7-day percent change
    """
    price: typing.Optional[float] = pydantic.Field(alias="price", default=None)
    """
    Current price in USD
    """
    symbol_field: typing.Optional[str] = pydantic.Field(alias="symbol", default=None)
    """
    Asset symbol
    """
    updated_at: typing.Optional[str] = pydantic.Field(alias="updated_at", default=None)
    """
    Timestamp of the price update
    """
