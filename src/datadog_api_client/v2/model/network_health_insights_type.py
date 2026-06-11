# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class NetworkHealthInsightsType(ModelSimple):
    """
    The resource type for network health insights. Always `network-health-insights`.

    :param value: If omitted defaults to "network-health-insights". Must be one of ["network-health-insights"].
    :type value: str
    """

    allowed_values = {
        "network-health-insights",
    }
    NETWORK_HEALTH_INSIGHTS: ClassVar["NetworkHealthInsightsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


NetworkHealthInsightsType.NETWORK_HEALTH_INSIGHTS = NetworkHealthInsightsType("network-health-insights")
