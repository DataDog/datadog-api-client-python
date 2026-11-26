# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class StructuredAnalysisCalculatedFieldType(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: If omitted defaults to "calculated_field". Must be one of ["calculated_field"].
    :type value: str
    """

    allowed_values = {
        "calculated_field",
    }
    CALCULATED_FIELD: ClassVar["StructuredAnalysisCalculatedFieldType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


StructuredAnalysisCalculatedFieldType.CALCULATED_FIELD = StructuredAnalysisCalculatedFieldType("calculated_field")
