import pydantic
import typing_extensions


class TokenRequest(typing_extensions.TypedDict):
    """
    TokenRequest
    """

    client_id: typing_extensions.Required[str]
    """
    Client ID provided by Turnqey
    """

    client_secret: typing_extensions.Required[str]
    """
    Client secret provided by Turnqey
    """


class _SerializerTokenRequest(pydantic.BaseModel):
    """
    Serializer for TokenRequest handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    client_id: str = pydantic.Field(
        alias="client_id",
    )
    client_secret: str = pydantic.Field(
        alias="client_secret",
    )
