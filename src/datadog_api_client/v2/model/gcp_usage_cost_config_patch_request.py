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
    from datadog_api_client.v2.model.gcp_usage_cost_config_patch_data import GCPUsageCostConfigPatchData


class GCPUsageCostConfigPatchRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.gcp_usage_cost_config_patch_data import GCPUsageCostConfigPatchData

        return {
            "data": (GCPUsageCostConfigPatchData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: GCPUsageCostConfigPatchData, **kwargs):
        """
        GCP Usage Cost config patch request.

        :param data: GCP Usage Cost config patch data.
        :type data: GCPUsageCostConfigPatchData
        """
        super().__init__(kwargs)

        self_.data = data
