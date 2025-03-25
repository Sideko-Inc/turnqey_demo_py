import pydantic
import typing


class Advisor(pydantic.BaseModel):
    """
    Advisor
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    company: typing.Optional[str] = pydantic.Field(alias="company", default=None)
    """
    Company name of the advisor
    """
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    """
    Timestamp when advisor was created
    """
    email_field: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    """
    Email address of the advisor
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    Unique identifier for the advisor
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    Full name of the advisor
    """
    updated_at: typing.Optional[str] = pydantic.Field(alias="updated_at", default=None)
    """
    Timestamp when advisor was last updated
    """
