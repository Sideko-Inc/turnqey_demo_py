import pydantic
import typing
import typing_extensions


class Trade(pydantic.BaseModel):
    """
    Trade
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    base_asset: typing.Optional[str] = pydantic.Field(alias="base_asset", default=None)
    """
    Base asset in the trading pair
    """
    base_quantity: typing.Optional[float] = pydantic.Field(
        alias="base_quantity", default=None
    )
    """
    Quantity of base asset
    """
    client_id: typing.Optional[str] = pydantic.Field(alias="client_id", default=None)
    """
    ID of the client
    """
    exchange_id: typing.Optional[str] = pydantic.Field(
        alias="exchange_id", default=None
    )
    """
    ID of the exchange where the trade occurred
    """
    fee: typing.Optional[float] = pydantic.Field(alias="fee", default=None)
    """
    Fee paid for the trade
    """
    fee_asset: typing.Optional[str] = pydantic.Field(alias="fee_asset", default=None)
    """
    Asset in which the fee was paid
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    Unique identifier for the trade
    """
    price: typing.Optional[float] = pydantic.Field(alias="price", default=None)
    """
    Trade price
    """
    quote_asset: typing.Optional[str] = pydantic.Field(
        alias="quote_asset", default=None
    )
    """
    Quote asset in the trading pair
    """
    quote_quantity: typing.Optional[float] = pydantic.Field(
        alias="quote_quantity", default=None
    )
    """
    Quantity of quote asset
    """
    timestamp: typing.Optional[str] = pydantic.Field(alias="timestamp", default=None)
    """
    When the trade occurred
    """
    trade_type: typing.Optional[typing_extensions.Literal["buy", "sell"]] = (
        pydantic.Field(alias="trade_type", default=None)
    )
    """
    Type of trade
    """
