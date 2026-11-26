# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RetentionCurveDefinitionType(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: If omitted defaults to "retention_curve". Must be one of ["retention_curve"].
    :type value: str
    """

    allowed_values = {
        "retention_curve",
    }
    RETENTION_CURVE: ClassVar["RetentionCurveDefinitionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RetentionCurveDefinitionType.RETENTION_CURVE = RetentionCurveDefinitionType("retention_curve")
