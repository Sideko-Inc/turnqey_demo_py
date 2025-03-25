import pydantic
import typing
import typing_extensions


class ClientUpdate(typing_extensions.TypedDict):
    """
    ClientUpdate
    """

    email_field: typing_extensions.NotRequired[str]
    """
    Email address of the client
    """

    name: typing_extensions.NotRequired[str]
    """
    Full name of the client
    """

    phone: typing_extensions.NotRequired[str]
    """
    Phone number of the client
    """


class _SerializerClientUpdate(pydantic.BaseModel):
    """
    Serializer for ClientUpdate handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    email_field: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
