import pydantic
import typing

from .balance import Balance
from .pagination import Pagination


class ClientsBalancesGetResponse(pydantic.BaseModel):
    """
    ClientsBalancesGetResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[Balance]] = pydantic.Field(
        alias="data", default=None
    )
    pagination: typing.Optional[Pagination] = pydantic.Field(
        alias="pagination", default=None
    )
