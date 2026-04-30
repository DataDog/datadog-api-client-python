# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumPermanentRetentionFilterType(ModelSimple):
    """
    The resource type. The value must be `permanent_retention_filters`.

    :param value: If omitted defaults to "permanent_retention_filters". Must be one of ["permanent_retention_filters"].
    :type value: str
    """

    allowed_values = {
        "permanent_retention_filters",
    }
    PERMANENT_RETENTION_FILTERS: ClassVar["RumPermanentRetentionFilterType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumPermanentRetentionFilterType.PERMANENT_RETENTION_FILTERS = RumPermanentRetentionFilterType(
    "permanent_retention_filters"
)
