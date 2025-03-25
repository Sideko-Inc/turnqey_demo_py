import pydantic
import typing
import typing_extensions


class Transfer(pydantic.BaseModel):
    """
    Transfer
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    asset: typing.Optional[str] = pydantic.Field(alias="asset", default=None)
    """
    Asset being transferred
    """
    client_id: typing.Optional[str] = pydantic.Field(alias="client_id", default=None)
    """
    ID of the client
    """
    destination_id: typing.Optional[str] = pydantic.Field(
        alias="destination_id", default=None
    )
    """
    ID of the destination wallet or exchange
    """
    destination_type: typing.Optional[
        typing_extensions.Literal["exchange", "wallet"]
    ] = pydantic.Field(alias="destination_type", default=None)
    """
    Type of destination
    """
    fee: typing.Optional[float] = pydantic.Field(alias="fee", default=None)
    """
    Fee paid for the transfer
    """
    fee_asset: typing.Optional[str] = pydantic.Field(alias="fee_asset", default=None)
    """
    Asset in which the fee was paid
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    Unique identifier for the transfer
    """
    quantity: typing.Optional[float] = pydantic.Field(alias="quantity", default=None)
    """
    Quantity transferred
    """
    source_id: typing.Optional[str] = pydantic.Field(alias="source_id", default=None)
    """
    ID of the source wallet or exchange
    """
    source_type: typing.Optional[typing_extensions.Literal["exchange", "wallet"]] = (
        pydantic.Field(alias="source_type", default=None)
    )
    """
    Type of source
    """
    status: typing.Optional[
        typing_extensions.Literal["completed", "failed", "pending"]
    ] = pydantic.Field(alias="status", default=None)
    """
    Status of the transfer
    """
    timestamp: typing.Optional[str] = pydantic.Field(alias="timestamp", default=None)
    """
    When the transfer occurred
    """
