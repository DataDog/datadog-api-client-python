# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CaseType(ModelSimple):
    """
    Case type

    :param value: Must be one of ["STANDARD", "TUNKNOWN"].
    :type value: str
    """

    allowed_values = {
        "STANDARD",
        "TUNKNOWN",
    }
    STANDARD: ClassVar["CaseType"]
    TUNKNOWN: ClassVar["CaseType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CaseType.STANDARD = CaseType("STANDARD")
CaseType.TUNKNOWN = CaseType("TUNKNOWN")
