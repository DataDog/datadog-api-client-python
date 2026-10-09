# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SeverityOverrideDataType(ModelSimple):
    """
    Severity override resource type.

    :param value: If omitted defaults to "severity_override". Must be one of ["severity_override"].
    :type value: str
    """

    allowed_values = {
        "severity_override",
    }
    SEVERITY_OVERRIDE: ClassVar["SeverityOverrideDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SeverityOverrideDataType.SEVERITY_OVERRIDE = SeverityOverrideDataType("severity_override")
