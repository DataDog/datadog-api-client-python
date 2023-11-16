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
    from datadog_api_client.v2.model.projected_cost_attributes import ProjectedCostAttributes
    from datadog_api_client.v2.model.projected_cost_type import ProjectedCostType


class ProjectedCost(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.projected_cost_attributes import ProjectedCostAttributes
        from datadog_api_client.v2.model.projected_cost_type import ProjectedCostType

        return {
            "attributes": (ProjectedCostAttributes,),
            "id": (str,),
            "type": (ProjectedCostType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[ProjectedCostAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[ProjectedCostType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Projected Cost data.

        :param attributes: Projected Cost attributes data.
        :type attributes: ProjectedCostAttributes, optional

        :param id: Unique ID of the response.
        :type id: str, optional

        :param type: Type of cost data.
        :type type: ProjectedCostType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
