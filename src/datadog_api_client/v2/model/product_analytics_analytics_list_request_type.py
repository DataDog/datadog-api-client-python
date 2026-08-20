# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsAnalyticsListRequestType(ModelSimple):
    """
    The resource type for analytics list requests.

    :param value: If omitted defaults to "formula_analytics_extended_list_request". Must be one of ["formula_analytics_extended_list_request"].
    :type value: str
    """

    allowed_values = {
        "formula_analytics_extended_list_request",
    }
    FORMULA_ANALYTICS_EXTENDED_LIST_REQUEST: ClassVar["ProductAnalyticsAnalyticsListRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsAnalyticsListRequestType.FORMULA_ANALYTICS_EXTENDED_LIST_REQUEST = (
    ProductAnalyticsAnalyticsListRequestType("formula_analytics_extended_list_request")
)
