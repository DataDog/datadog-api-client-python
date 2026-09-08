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
    from datadog_api_client.v2.model.unit_cost_data_response import UnitCostDataResponse


class UnitCostResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.unit_cost_data_response import UnitCostDataResponse

        return {
            "data": (UnitCostDataResponse,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: UnitCostDataResponse, **kwargs):
        """
        A response containing a single unit cost.

        :param data: The data object of a unit cost response.
        :type data: UnitCostDataResponse
        """
        super().__init__(kwargs)

        self_.data = data
