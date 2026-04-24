# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsTestResultSummaryType(ModelSimple):
    """
    Type of the Synthetic test result summary resource, `result_summary`.

    :param value: If omitted defaults to "result_summary". Must be one of ["result_summary"].
    :type value: str
    """

    allowed_values = {
        "result_summary",
    }
    RESULT_SUMMARY: ClassVar["SyntheticsTestResultSummaryType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsTestResultSummaryType.RESULT_SUMMARY = SyntheticsTestResultSummaryType("result_summary")
