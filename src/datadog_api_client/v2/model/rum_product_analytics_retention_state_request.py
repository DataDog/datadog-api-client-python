# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RUMProductAnalyticsRetentionStateRequest(ModelSimple):
    """
    Retention policy to set for Product Analytics data derived from RUM events. `PREVIEW` is the initial state of a new application and is reported as `NONE` in responses. Setting `MAX` requires the `product_analytics_apps_write` permission.

    :param value: Must be one of ["MAX", "NONE", "PREVIEW"].
    :type value: str
    """

    allowed_values = {
        "MAX",
        "NONE",
        "PREVIEW",
    }
    MAX: ClassVar["RUMProductAnalyticsRetentionStateRequest"]
    NONE: ClassVar["RUMProductAnalyticsRetentionStateRequest"]
    PREVIEW: ClassVar["RUMProductAnalyticsRetentionStateRequest"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RUMProductAnalyticsRetentionStateRequest.MAX = RUMProductAnalyticsRetentionStateRequest("MAX")
RUMProductAnalyticsRetentionStateRequest.NONE = RUMProductAnalyticsRetentionStateRequest("NONE")
RUMProductAnalyticsRetentionStateRequest.PREVIEW = RUMProductAnalyticsRetentionStateRequest("PREVIEW")
