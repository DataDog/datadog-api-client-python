# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsAnalyticsRequestType(ModelSimple):
    """
    The resource type for analytics requests.

    :param value: If omitted defaults to "formula_analytics_extended_request". Must be one of ["formula_analytics_extended_request"].
    :type value: str
    """

    allowed_values = {
        "formula_analytics_extended_request",
    }
    FORMULA_ANALYTICS_EXTENDED_REQUEST: ClassVar["ProductAnalyticsAnalyticsRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsAnalyticsRequestType.FORMULA_ANALYTICS_EXTENDED_REQUEST = ProductAnalyticsAnalyticsRequestType(
    "formula_analytics_extended_request"
)
