# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsRetentionListRequestType(ModelSimple):
    """
    The resource type identifier for a retention list request.

    :param value: If omitted defaults to "retention_list_request". Must be one of ["retention_list_request"].
    :type value: str
    """

    allowed_values = {
        "retention_list_request",
    }
    RETENTION_LIST_REQUEST: ClassVar["ProductAnalyticsRetentionListRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsRetentionListRequestType.RETENTION_LIST_REQUEST = ProductAnalyticsRetentionListRequestType(
    "retention_list_request"
)
