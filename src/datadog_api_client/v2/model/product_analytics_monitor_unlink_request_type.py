# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsMonitorUnlinkRequestType(ModelSimple):
    """
    Product Analytics monitor unlink request resource type.

    :param value: If omitted defaults to "pa_monitor_unlink_request". Must be one of ["pa_monitor_unlink_request"].
    :type value: str
    """

    allowed_values = {
        "pa_monitor_unlink_request",
    }
    PA_MONITOR_UNLINK_REQUEST: ClassVar["ProductAnalyticsMonitorUnlinkRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsMonitorUnlinkRequestType.PA_MONITOR_UNLINK_REQUEST = ProductAnalyticsMonitorUnlinkRequestType(
    "pa_monitor_unlink_request"
)
