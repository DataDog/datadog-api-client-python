# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.monthly_cost_attribution_attributes import MonthlyCostAttributionAttributes
    from datadog_api_client.v2.model.cost_attribution_type import CostAttributionType


class MonthlyCostAttributionBody(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.monthly_cost_attribution_attributes import MonthlyCostAttributionAttributes
        from datadog_api_client.v2.model.cost_attribution_type import CostAttributionType

        return {
            "attributes": (MonthlyCostAttributionAttributes,),
            "id": (str,),
            "type": (CostAttributionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[MonthlyCostAttributionAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[CostAttributionType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Cost data.

        :param attributes: Cost Attribution by Tag for a given organization.
        :type attributes: MonthlyCostAttributionAttributes, optional

        :param id: Unique ID of the response.
        :type id: str, optional

        :param type: Type of cost attribution data.
        :type type: CostAttributionType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
