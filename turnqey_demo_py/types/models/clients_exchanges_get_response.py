import pydantic
import typing

from .exchange import Exchange
from .pagination import Pagination


class ClientsExchangesGetResponse(pydantic.BaseModel):
    """
    ClientsExchangesGetResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[Exchange]] = pydantic.Field(
        alias="data", default=None
    )
    pagination: typing.Optional[Pagination] = pydantic.Field(
        alias="pagination", default=None
    )
