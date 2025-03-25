import pydantic
import typing
import typing_extensions


class WalletCreate(typing_extensions.TypedDict):
    """
    WalletCreate
    """

    address: typing_extensions.Required[str]
    """
    Blockchain address of the wallet
    """

    blockchain: typing_extensions.Required[str]
    """
    Blockchain network (e.g. Ethereum, Bitcoin)
    """

    label: typing_extensions.NotRequired[str]
    """
    User-defined label for the wallet
    """


class _SerializerWalletCreate(pydantic.BaseModel):
    """
    Serializer for WalletCreate handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: str = pydantic.Field(
        alias="address",
    )
    blockchain: str = pydantic.Field(
        alias="blockchain",
    )
    label: typing.Optional[str] = pydantic.Field(alias="label", default=None)
