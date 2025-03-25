import pydantic
import typing

from .pagination import Pagination
from .wallet import Wallet


class ClientsWalletsListResponse(pydantic.BaseModel):
    """
    ClientsWalletsListResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[Wallet]] = pydantic.Field(
        alias="data", default=None
    )
    pagination: typing.Optional[Pagination] = pydantic.Field(
        alias="pagination", default=None
    )
