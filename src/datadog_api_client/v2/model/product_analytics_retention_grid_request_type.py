# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsRetentionGridRequestType(ModelSimple):
    """
    The resource type identifier for a retention grid request.

    :param value: If omitted defaults to "retention_grid_request". Must be one of ["retention_grid_request"].
    :type value: str
    """

    allowed_values = {
        "retention_grid_request",
    }
    RETENTION_GRID_REQUEST: ClassVar["ProductAnalyticsRetentionGridRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsRetentionGridRequestType.RETENTION_GRID_REQUEST = ProductAnalyticsRetentionGridRequestType(
    "retention_grid_request"
)
