import pydantic
import typing
import typing_extensions


class ClientCreate(typing_extensions.TypedDict):
    """
    ClientCreate
    """

    email_field: typing_extensions.Required[str]
    """
    Email address of the client
    """

    name: typing_extensions.Required[str]
    """
    Full name of the client
    """

    phone: typing_extensions.NotRequired[str]
    """
    Phone number of the client
    """


class _SerializerClientCreate(pydantic.BaseModel):
    """
    Serializer for ClientCreate handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    email_field: str = pydantic.Field(
        alias="email",
    )
    name: str = pydantic.Field(
        alias="name",
    )
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
