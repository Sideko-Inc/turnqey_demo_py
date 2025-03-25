import pydantic
import typing


class TokenResponse(pydantic.BaseModel):
    """
    TokenResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    access_token: typing.Optional[str] = pydantic.Field(
        alias="access_token", default=None
    )
    """
    JWT token for API authentication
    """
    expires_in: typing.Optional[int] = pydantic.Field(alias="expires_in", default=None)
    """
    Token expiration time in seconds
    """
    token_type: typing.Optional[str] = pydantic.Field(alias="token_type", default=None)
    """
    Type of token (always "Bearer")
    """
