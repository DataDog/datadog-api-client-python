# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MonitorAssetCategory(ModelSimple):
    """
    Indicates the type of asset this entity represents on a monitor.

    :param value: Must be one of ["dashboard", "workflow", "runbook"].
    :type value: str
    """

    allowed_values = {
        "dashboard",
        "workflow",
        "runbook",
    }
    DASHBOARD: ClassVar["MonitorAssetCategory"]
    WORKFLOW: ClassVar["MonitorAssetCategory"]
    RUNBOOK: ClassVar["MonitorAssetCategory"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MonitorAssetCategory.DASHBOARD = MonitorAssetCategory("dashboard")
MonitorAssetCategory.WORKFLOW = MonitorAssetCategory("workflow")
MonitorAssetCategory.RUNBOOK = MonitorAssetCategory("runbook")
