# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsMonitorListType(ModelSimple):
    """
    Product Analytics monitor list resource type.

    :param value: If omitted defaults to "pa_monitor_list". Must be one of ["pa_monitor_list"].
    :type value: str
    """

    allowed_values = {
        "pa_monitor_list",
    }
    PA_MONITOR_LIST: ClassVar["ProductAnalyticsMonitorListType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsMonitorListType.PA_MONITOR_LIST = ProductAnalyticsMonitorListType("pa_monitor_list")
