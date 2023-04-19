# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FindingType(ModelSimple):
    """
    The JSON:API type for findings.

    :param value: If omitted defaults to "finding". Must be one of ["finding"].
    :type value: str
    """

    allowed_values = {
        "finding",
    }
    FINDING: ClassVar["FindingType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FindingType.FINDING = FindingType("finding")
