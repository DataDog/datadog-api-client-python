# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsAnalyticsListResponseType(ModelSimple):
    """
    The resource type identifier for an analytics list response.

    :param value: If omitted defaults to "list_response". Must be one of ["list_response"].
    :type value: str
    """

    allowed_values = {
        "list_response",
    }
    LIST_RESPONSE: ClassVar["ProductAnalyticsAnalyticsListResponseType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsAnalyticsListResponseType.LIST_RESPONSE = ProductAnalyticsAnalyticsListResponseType("list_response")
