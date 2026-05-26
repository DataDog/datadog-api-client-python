# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AnalysisEditType(ModelSimple):
    """
    The type of code edit to apply when fixing a violation.

    :param value: If omitted defaults to "ADD". Must be one of ["ADD", "UPDATE", "REMOVE"].
    :type value: str
    """

    allowed_values = {
        "ADD",
        "UPDATE",
        "REMOVE",
    }
    ADD: ClassVar["AnalysisEditType"]
    UPDATE: ClassVar["AnalysisEditType"]
    REMOVE: ClassVar["AnalysisEditType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AnalysisEditType.ADD = AnalysisEditType("ADD")
AnalysisEditType.UPDATE = AnalysisEditType("UPDATE")
AnalysisEditType.REMOVE = AnalysisEditType("REMOVE")
