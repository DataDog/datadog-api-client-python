# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CasePriority(ModelSimple):
    """
    Case priority

    :param value: If omitted defaults to "NOT_DEFINED". Must be one of ["NOT_DEFINED", "P1", "P2", "P3", "P4", "P5"].
    :type value: str
    """

    allowed_values = {
        "NOT_DEFINED",
        "P1",
        "P2",
        "P3",
        "P4",
        "P5",
    }
    NOT_DEFINED: ClassVar["CasePriority"]
    P1: ClassVar["CasePriority"]
    P2: ClassVar["CasePriority"]
    P3: ClassVar["CasePriority"]
    P4: ClassVar["CasePriority"]
    P5: ClassVar["CasePriority"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CasePriority.NOT_DEFINED = CasePriority("NOT_DEFINED")
CasePriority.P1 = CasePriority("P1")
CasePriority.P2 = CasePriority("P2")
CasePriority.P3 = CasePriority("P3")
CasePriority.P4 = CasePriority("P4")
CasePriority.P5 = CasePriority("P5")
