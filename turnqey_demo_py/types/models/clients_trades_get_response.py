import pydantic
import typing

from .pagination import Pagination
from .trade import Trade


class ClientsTradesGetResponse(pydantic.BaseModel):
    """
    ClientsTradesGetResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[Trade]] = pydantic.Field(
        alias="data", default=None
    )
    pagination: typing.Optional[Pagination] = pydantic.Field(
        alias="pagination", default=None
    )
