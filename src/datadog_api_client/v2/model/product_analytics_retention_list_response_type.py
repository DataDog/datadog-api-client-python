# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsRetentionListResponseType(ModelSimple):
    """
    The resource type identifier for a retention list response.

    :param value: If omitted defaults to "retention_list_response". Must be one of ["retention_list_response"].
    :type value: str
    """

    allowed_values = {
        "retention_list_response",
    }
    RETENTION_LIST_RESPONSE: ClassVar["ProductAnalyticsRetentionListResponseType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsRetentionListResponseType.RETENTION_LIST_RESPONSE = ProductAnalyticsRetentionListResponseType(
    "retention_list_response"
)
