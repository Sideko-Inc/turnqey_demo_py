import pydantic
import typing


class HoldingPrice(pydantic.BaseModel):
    """
    HoldingPrice
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    market_cap: typing.Optional[float] = pydantic.Field(
        alias="market_cap", default=None
    )
    """
    Market capitalization in USD
    """
    percent_change_24h: typing.Optional[float] = pydantic.Field(
        alias="percent_change_24h", default=None
    )
    """
    24-hour percent change
    """
    price: typing.Optional[float] = pydantic.Field(alias="price", default=None)
    """
    Price in USD
    """
    symbol_field: typing.Optional[str] = pydantic.Field(alias="symbol", default=None)
    """
    Asset symbol
    """
    timestamp: typing.Optional[str] = pydantic.Field(alias="timestamp", default=None)
    """
    Timestamp of the price
    """
    volume_24h: typing.Optional[float] = pydantic.Field(
        alias="volume_24h", default=None
    )
    """
    24-hour trading volume in USD
    """
