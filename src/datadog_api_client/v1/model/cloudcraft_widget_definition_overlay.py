# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CloudcraftWidgetDefinitionOverlay(ModelSimple):
    """
    Overlay applied on top of the Cloudcraft topology.

    :param value: Must be one of ["Observability", "CloudCost", "Security", "NDMReachability", "Monitors", "APM", "Default"].
    :type value: str
    """

    allowed_values = {
        "Observability",
        "CloudCost",
        "Security",
        "NDMReachability",
        "Monitors",
        "APM",
        "Default",
    }
    OBSERVABILITY: ClassVar["CloudcraftWidgetDefinitionOverlay"]
    CLOUD_COST: ClassVar["CloudcraftWidgetDefinitionOverlay"]
    SECURITY: ClassVar["CloudcraftWidgetDefinitionOverlay"]
    NDM_REACHABILITY: ClassVar["CloudcraftWidgetDefinitionOverlay"]
    MONITORS: ClassVar["CloudcraftWidgetDefinitionOverlay"]
    APM: ClassVar["CloudcraftWidgetDefinitionOverlay"]
    DEFAULT: ClassVar["CloudcraftWidgetDefinitionOverlay"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CloudcraftWidgetDefinitionOverlay.OBSERVABILITY = CloudcraftWidgetDefinitionOverlay("Observability")
CloudcraftWidgetDefinitionOverlay.CLOUD_COST = CloudcraftWidgetDefinitionOverlay("CloudCost")
CloudcraftWidgetDefinitionOverlay.SECURITY = CloudcraftWidgetDefinitionOverlay("Security")
CloudcraftWidgetDefinitionOverlay.NDM_REACHABILITY = CloudcraftWidgetDefinitionOverlay("NDMReachability")
CloudcraftWidgetDefinitionOverlay.MONITORS = CloudcraftWidgetDefinitionOverlay("Monitors")
CloudcraftWidgetDefinitionOverlay.APM = CloudcraftWidgetDefinitionOverlay("APM")
CloudcraftWidgetDefinitionOverlay.DEFAULT = CloudcraftWidgetDefinitionOverlay("Default")
