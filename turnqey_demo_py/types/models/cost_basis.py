import pydantic
import typing


class CostBasis(pydantic.BaseModel):
    """
    CostBasis
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    acquisition_date: typing.Optional[str] = pydantic.Field(
        alias="acquisition_date", default=None
    )
    """
    Date when the asset was acquired
    """
    asset: typing.Optional[str] = pydantic.Field(alias="asset", default=None)
    """
    Asset symbol (e.g. BTC, ETH)
    """
    client_id: typing.Optional[str] = pydantic.Field(alias="client_id", default=None)
    """
    ID of the client
    """
    cost_basis: typing.Optional[float] = pydantic.Field(
        alias="cost_basis", default=None
    )
    """
    Total cost basis in USD
    """
    cost_per_unit: typing.Optional[float] = pydantic.Field(
        alias="cost_per_unit", default=None
    )
    """
    Cost per unit in USD
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    Unique identifier for the cost basis record
    """
    quantity: typing.Optional[float] = pydantic.Field(alias="quantity", default=None)
    """
    Asset quantity
    """
