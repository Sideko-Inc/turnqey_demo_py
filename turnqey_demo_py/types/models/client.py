import pydantic
import typing


class Client(pydantic.BaseModel):
    """
    Client
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    """
    Timestamp when client was created
    """
    email_field: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    """
    Email address of the client
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    Unique identifier for the client
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    Full name of the client
    """
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    """
    Phone number of the client
    """
    updated_at: typing.Optional[str] = pydantic.Field(alias="updated_at", default=None)
    """
    Timestamp when client was last updated
    """
