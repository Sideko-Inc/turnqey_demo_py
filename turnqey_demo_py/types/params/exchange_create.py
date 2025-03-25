import pydantic
import typing_extensions


class ExchangeCreate(typing_extensions.TypedDict):
    """
    ExchangeCreate
    """

    api_key: typing_extensions.Required[str]
    """
    API key for the exchange
    """

    api_secret: typing_extensions.Required[str]
    """
    API secret for the exchange
    """

    exchange_name: typing_extensions.Required[str]
    """
    Name of the exchange
    """


class _SerializerExchangeCreate(pydantic.BaseModel):
    """
    Serializer for ExchangeCreate handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    api_key: str = pydantic.Field(
        alias="api_key",
    )
    api_secret: str = pydantic.Field(
        alias="api_secret",
    )
    exchange_name: str = pydantic.Field(
        alias="exchange_name",
    )
