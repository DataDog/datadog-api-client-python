# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.chargeback_breakdown import ChargebackBreakdown
from datadog_api_client.v2.model.chargeback_breakdown import ChargebackBreakdown

if TYPE_CHECKING:
    from datadog_api_client.v2.model.cost_by_org import CostByOrg


@dataclass
class CostByOrgResponseJSON:
    id: str
    charges: Union[List[ChargebackBreakdown], UnsetType] = unset
    date: Union[datetime, UnsetType] = unset
    org_name: Union[str, UnsetType] = unset
    public_id: Union[str, UnsetType] = unset
    region: Union[str, UnsetType] = unset
    total_cost: Union[float, UnsetType] = unset


class CostByOrgResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_by_org import CostByOrg

        return {
            "data": ([CostByOrg],),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = CostByOrgResponseJSON

    def __init__(self_, data: Union[List[CostByOrg], UnsetType] = unset, **kwargs):
        """
        Chargeback Summary response.

        :param data: Response containing Chargeback Summary.
        :type data: [CostByOrg], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
