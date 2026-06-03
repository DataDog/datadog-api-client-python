# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumHardcodedRetentionFilterType(ModelSimple):
    """
    The resource type. The value must be `hardcoded_retention_filters`.

    :param value: If omitted defaults to "hardcoded_retention_filters". Must be one of ["hardcoded_retention_filters"].
    :type value: str
    """

    allowed_values = {
        "hardcoded_retention_filters",
    }
    HARDCODED_RETENTION_FILTERS: ClassVar["RumHardcodedRetentionFilterType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumHardcodedRetentionFilterType.HARDCODED_RETENTION_FILTERS = RumHardcodedRetentionFilterType(
    "hardcoded_retention_filters"
)
