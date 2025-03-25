import pydantic
import typing

from .deposit_withdrawal import DepositWithdrawal
from .pagination import Pagination


class ClientsDepositsWithdrawalsGetResponse(pydantic.BaseModel):
    """
    ClientsDepositsWithdrawalsGetResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[DepositWithdrawal]] = pydantic.Field(
        alias="data", default=None
    )
    pagination: typing.Optional[Pagination] = pydantic.Field(
        alias="pagination", default=None
    )
