import pydantic
import typing
import typing_extensions


class Transaction(pydantic.BaseModel):
    """
    Transaction
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    asset: typing.Optional[str] = pydantic.Field(alias="asset", default=None)
    """
    Asset involved in the transaction
    """
    client_id: typing.Optional[str] = pydantic.Field(alias="client_id", default=None)
    """
    ID of the client
    """
    destination: typing.Optional[str] = pydantic.Field(
        alias="destination", default=None
    )
    """
    Destination of the transaction
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    Unique identifier for the transaction
    """
    quantity: typing.Optional[float] = pydantic.Field(alias="quantity", default=None)
    """
    Quantity of the asset
    """
    source: typing.Optional[str] = pydantic.Field(alias="source", default=None)
    """
    Source of the transaction
    """
    timestamp: typing.Optional[str] = pydantic.Field(alias="timestamp", default=None)
    """
    When the transaction occurred
    """
    transaction_type: typing.Optional[
        typing_extensions.Literal[
            "deposit", "fee", "reward", "trade", "transfer", "withdrawal"
        ]
    ] = pydantic.Field(alias="transaction_type", default=None)
    """
    Type of transaction
    """
    usd_value: typing.Optional[float] = pydantic.Field(alias="usd_value", default=None)
    """
    Value in USD at the time of the transaction
    """
