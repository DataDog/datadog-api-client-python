# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsMonitorRequestType(ModelSimple):
    """
    Product Analytics monitor request resource type.

    :param value: If omitted defaults to "pa_monitor_request". Must be one of ["pa_monitor_request"].
    :type value: str
    """

    allowed_values = {
        "pa_monitor_request",
    }
    PA_MONITOR_REQUEST: ClassVar["ProductAnalyticsMonitorRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsMonitorRequestType.PA_MONITOR_REQUEST = ProductAnalyticsMonitorRequestType("pa_monitor_request")
