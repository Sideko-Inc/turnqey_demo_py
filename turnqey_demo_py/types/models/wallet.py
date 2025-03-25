import pydantic
import typing


class Wallet(pydantic.BaseModel):
    """
    Wallet
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: typing.Optional[str] = pydantic.Field(alias="address", default=None)
    """
    Blockchain address of the wallet
    """
    blockchain: typing.Optional[str] = pydantic.Field(alias="blockchain", default=None)
    """
    Blockchain network (e.g. Ethereum, Bitcoin)
    """
    client_id: typing.Optional[str] = pydantic.Field(alias="client_id", default=None)
    """
    ID of the client who owns this wallet
    """
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    """
    Timestamp when wallet was created
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    Unique identifier for the wallet
    """
    label: typing.Optional[str] = pydantic.Field(alias="label", default=None)
    """
    User-defined label for the wallet
    """
    updated_at: typing.Optional[str] = pydantic.Field(alias="updated_at", default=None)
    """
    Timestamp when wallet was last updated
    """
