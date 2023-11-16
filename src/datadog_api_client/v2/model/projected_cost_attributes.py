# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.chargeback_breakdown import ChargebackBreakdown


class ProjectedCostAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.chargeback_breakdown import ChargebackBreakdown

        return {
            "charges": ([ChargebackBreakdown],),
            "date": (datetime,),
            "org_name": (str,),
            "projected_total_cost": (float,),
            "public_id": (str,),
            "region": (str,),
        }

    attribute_map = {
        "charges": "charges",
        "date": "date",
        "org_name": "org_name",
        "projected_total_cost": "projected_total_cost",
        "public_id": "public_id",
        "region": "region",
    }

    def __init__(
        self_,
        charges: Union[List[ChargebackBreakdown], UnsetType] = unset,
        date: Union[datetime, UnsetType] = unset,
        org_name: Union[str, UnsetType] = unset,
        projected_total_cost: Union[float, UnsetType] = unset,
        public_id: Union[str, UnsetType] = unset,
        region: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Projected Cost attributes data.

        :param charges: List of charges data reported for the requested month.
        :type charges: [ChargebackBreakdown], optional

        :param date: The month requested.
        :type date: datetime, optional

        :param org_name: The organization name.
        :type org_name: str, optional

        :param projected_total_cost: The total projected cost of products for the month.
        :type projected_total_cost: float, optional

        :param public_id: The organization public ID.
        :type public_id: str, optional

        :param region: The region of the Datadog instance that the organization belongs to.
        :type region: str, optional
        """
        if charges is not unset:
            kwargs["charges"] = charges
        if date is not unset:
            kwargs["date"] = date
        if org_name is not unset:
            kwargs["org_name"] = org_name
        if projected_total_cost is not unset:
            kwargs["projected_total_cost"] = projected_total_cost
        if public_id is not unset:
            kwargs["public_id"] = public_id
        if region is not unset:
            kwargs["region"] = region
        super().__init__(kwargs)
