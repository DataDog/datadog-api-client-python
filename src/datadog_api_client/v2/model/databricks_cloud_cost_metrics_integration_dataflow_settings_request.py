# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class DatabricksCloudCostMetricsIntegrationDataflowSettingsRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "ccm_collect_all_workspaces": (bool,),
        }

    attribute_map = {
        "ccm_collect_all_workspaces": "ccm_collect_all_workspaces",
    }

    def __init__(self_, ccm_collect_all_workspaces: Union[bool, UnsetType] = unset, **kwargs):
        """
        Settings of the Databricks cloud cost metrics dataflow. Only the fields provided are changed.

        :param ccm_collect_all_workspaces: Whether cost data is collected for every workspace in the Databricks account rather than this workspace only.
        :type ccm_collect_all_workspaces: bool, optional
        """
        if ccm_collect_all_workspaces is not unset:
            kwargs["ccm_collect_all_workspaces"] = ccm_collect_all_workspaces
        super().__init__(kwargs)
