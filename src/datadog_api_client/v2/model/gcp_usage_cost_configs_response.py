# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
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

    def __init__(self_, data: Union[List[GCPUsageCostConfig], UnsetType] = unset, **kwargs):
        """
        List of GCP Usage Cost configs.

        :param data: A GCP Usage Cost config.
        :type data: [GCPUsageCostConfig], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
