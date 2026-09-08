# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.unit_cost_create_request_data import UnitCostCreateRequestData


class UnitCostCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.unit_cost_create_request_data import UnitCostCreateRequestData

        return {
            "data": (UnitCostCreateRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: UnitCostCreateRequestData, **kwargs):
        """
        A request to create a unit cost.

        :param data: The data object of a unit cost create request.
        :type data: UnitCostCreateRequestData
        """
        super().__init__(kwargs)

        self_.data = data
