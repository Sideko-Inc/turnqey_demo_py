import pydantic
import typing

from .cost_basis import CostBasis
from .pagination import Pagination


class ClientsCostbasisGetResponse(pydantic.BaseModel):
    """
    ClientsCostbasisGetResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[CostBasis]] = pydantic.Field(
        alias="data", default=None
    )
    pagination: typing.Optional[Pagination] = pydantic.Field(
        alias="pagination", default=None
    )
