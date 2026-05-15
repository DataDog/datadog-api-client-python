# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.cost_orchestrator import CostOrchestrator


class CostOrchestratorsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_orchestrator import CostOrchestrator

        return {
            "data": ([CostOrchestrator],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[CostOrchestrator], **kwargs):
        """
        List of container orchestrators detected in Cloud Cost Management data for the requested period.

        :param data: List of detected container orchestrators.
        :type data: [CostOrchestrator]
        """
        super().__init__(kwargs)

        self_.data = data
