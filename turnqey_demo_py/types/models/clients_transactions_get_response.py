import pydantic
import typing

from .pagination import Pagination
from .transaction import Transaction


class ClientsTransactionsGetResponse(pydantic.BaseModel):
    """
    ClientsTransactionsGetResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[Transaction]] = pydantic.Field(
        alias="data", default=None
    )
    pagination: typing.Optional[Pagination] = pydantic.Field(
        alias="pagination", default=None
    )
