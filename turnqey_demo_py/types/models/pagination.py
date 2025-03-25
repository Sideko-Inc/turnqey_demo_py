import pydantic
import typing


class Pagination(pydantic.BaseModel):
    """
    Pagination
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    limit: typing.Optional[int] = pydantic.Field(alias="limit", default=None)
    """
    Number of items per page
    """
    page: typing.Optional[int] = pydantic.Field(alias="page", default=None)
    """
    Current page number
    """
    pages: typing.Optional[int] = pydantic.Field(alias="pages", default=None)
    """
    Total number of pages
    """
    total: typing.Optional[int] = pydantic.Field(alias="total", default=None)
    """
    Total number of items
    """
