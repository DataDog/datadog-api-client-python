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
    from datadog_api_client.v2.model.gcp_usage_cost_config import GCPUsageCostConfig


class GCPUsageCostConfigsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.gcp_usage_cost_config import GCPUsageCostConfig

        return {
            "data": ([GCPUsageCostConfig],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[GCPUsageCostConfig], **kwargs):
        """
        List of Google Cloud Usage Cost configs.

        :param data: A Google Cloud Usage Cost config.
        :type data: [GCPUsageCostConfig]
        """
        super().__init__(kwargs)

        self_.data = data
