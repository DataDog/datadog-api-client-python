# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumRetentionFilterType(ModelSimple):
    """
    The type of the resource. The value should always be retention_filters.

    :param value: If omitted defaults to "retention_filters". Must be one of ["retention_filters"].
    :type value: str
    """

    allowed_values = {
        "retention_filters",
    }
    RETENTION_FILTERS: ClassVar["RumRetentionFilterType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumRetentionFilterType.RETENTION_FILTERS = RumRetentionFilterType("retention_filters")
