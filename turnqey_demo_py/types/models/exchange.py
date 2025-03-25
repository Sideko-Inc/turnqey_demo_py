import pydantic
import typing
import typing_extensions


class Exchange(pydantic.BaseModel):
    """
    Exchange
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    api_key: typing.Optional[str] = pydantic.Field(alias="api_key", default=None)
    """
    API key for the exchange (masked)
    """
    client_id: typing.Optional[str] = pydantic.Field(alias="client_id", default=None)
    """
    ID of the client who owns this exchange account
    """
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    """
    Timestamp when exchange was added
    """
    exchange_name: typing.Optional[str] = pydantic.Field(
        alias="exchange_name", default=None
    )
    """
    Name of the exchange
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    Unique identifier for the exchange
    """
    status: typing.Optional[
        typing_extensions.Literal["active", "inactive", "pending"]
    ] = pydantic.Field(alias="status", default=None)
    """
    Current status of the exchange connection
    """
    updated_at: typing.Optional[str] = pydantic.Field(alias="updated_at", default=None)
    """
    Timestamp when exchange was last updated
    """
