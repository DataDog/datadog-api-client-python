# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ApmRetentionFilterType(ModelSimple):
    """
    The type of the resource.

    :param value: If omitted defaults to "apm_retention_filter". Must be one of ["apm_retention_filter"].
    :type value: str
    """

    allowed_values = {
        "apm_retention_filter",
    }
    apm_retention_filter: ClassVar["ApmRetentionFilterType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ApmRetentionFilterType.apm_retention_filter = ApmRetentionFilterType("apm_retention_filter")
