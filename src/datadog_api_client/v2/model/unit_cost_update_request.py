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
    from datadog_api_client.v2.model.unit_cost_update_request_data import UnitCostUpdateRequestData


class UnitCostUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.unit_cost_update_request_data import UnitCostUpdateRequestData

        return {
            "data": (UnitCostUpdateRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: UnitCostUpdateRequestData, **kwargs):
        """
        A request to replace a unit cost.

        :param data: The data object of a unit cost replace request.
        :type data: UnitCostUpdateRequestData
        """
        super().__init__(kwargs)

        self_.data = data
