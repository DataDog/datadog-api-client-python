# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.unit_cost_data_attributes_response import UnitCostDataAttributesResponse
    from datadog_api_client.v2.model.unit_cost_type import UnitCostType


class UnitCostDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.unit_cost_data_attributes_response import UnitCostDataAttributesResponse
        from datadog_api_client.v2.model.unit_cost_type import UnitCostType

        return {
            "attributes": (UnitCostDataAttributesResponse,),
            "id": (UUID,),
            "type": (UnitCostType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: UnitCostDataAttributesResponse, id: UUID, type: UnitCostType, **kwargs):
        """
        The data object of a unit cost response.

        :param attributes: The attributes of a unit cost.
        :type attributes: UnitCostDataAttributesResponse

        :param id: The UUID of the unit cost.
        :type id: UUID

        :param type: The JSON:API resource type for a unit cost.
        :type type: UnitCostType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
