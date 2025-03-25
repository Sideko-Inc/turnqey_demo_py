import pydantic
import typing

from .pagination import Pagination
from .transfer import Transfer


class ClientsTransfersGetResponse(pydantic.BaseModel):
    """
    ClientsTransfersGetResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[Transfer]] = pydantic.Field(
        alias="data", default=None
    )
    pagination: typing.Optional[Pagination] = pydantic.Field(
        alias="pagination", default=None
    )
