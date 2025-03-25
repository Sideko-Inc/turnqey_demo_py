import pydantic
import typing

from .holding_price import HoldingPrice
from .pagination import Pagination


class PricesHoldingGetResponse(pydantic.BaseModel):
    """
    PricesHoldingGetResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[HoldingPrice]] = pydantic.Field(
        alias="data", default=None
    )
    pagination: typing.Optional[Pagination] = pydantic.Field(
        alias="pagination", default=None
    )
