import pydantic
import typing


class TotalDepositWithdrawal(pydantic.BaseModel):
    """
    TotalDepositWithdrawal
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    client_id: typing.Optional[str] = pydantic.Field(alias="client_id", default=None)
    """
    ID of the client
    """
    net_flow: typing.Optional[float] = pydantic.Field(alias="net_flow", default=None)
    """
    Net flow (deposits - withdrawals)
    """
    period_end: typing.Optional[str] = pydantic.Field(alias="period_end", default=None)
    """
    End date of the period
    """
    period_start: typing.Optional[str] = pydantic.Field(
        alias="period_start", default=None
    )
    """
    Start date of the period
    """
    total_deposits: typing.Optional[float] = pydantic.Field(
        alias="total_deposits", default=None
    )
    """
    Total USD value of all deposits
    """
    total_withdrawals: typing.Optional[float] = pydantic.Field(
        alias="total_withdrawals", default=None
    )
    """
    Total USD value of all withdrawals
    """
