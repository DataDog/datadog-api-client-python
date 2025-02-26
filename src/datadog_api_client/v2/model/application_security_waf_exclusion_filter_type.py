# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ApplicationSecurityWafExclusionFilterType(ModelSimple):
    """
    Type of the resource. The value should always be `exclusion_filter`.

    :param value: If omitted defaults to "exclusion_filter". Must be one of ["exclusion_filter"].
    :type value: str
    """

    allowed_values = {
        "exclusion_filter",
    }
    EXCLUSION_FILTER: ClassVar["ApplicationSecurityWafExclusionFilterType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ApplicationSecurityWafExclusionFilterType.EXCLUSION_FILTER = ApplicationSecurityWafExclusionFilterType(
    "exclusion_filter"
)
