# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DetailedFindingType(ModelSimple):
    """
    The JSON:API type for findings that have the message and resource configuration.

    :param value: If omitted defaults to "detailed_finding". Must be one of ["detailed_finding"].
    :type value: str
    """

    allowed_values = {
        "detailed_finding",
    }
    DETAILED_FINDING: ClassVar["DetailedFindingType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DetailedFindingType.DETAILED_FINDING = DetailedFindingType("detailed_finding")
