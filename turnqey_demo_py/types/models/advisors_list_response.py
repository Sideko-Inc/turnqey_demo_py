import pydantic
import typing

from .advisor import Advisor
from .pagination import Pagination


class AdvisorsListResponse(pydantic.BaseModel):
    """
    AdvisorsListResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[Advisor]] = pydantic.Field(
        alias="data", default=None
    )
    pagination: typing.Optional[Pagination] = pydantic.Field(
        alias="pagination", default=None
    )
