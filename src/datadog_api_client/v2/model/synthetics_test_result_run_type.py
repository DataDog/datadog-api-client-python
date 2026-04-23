# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsTestResultRunType(ModelSimple):
    """
    The type of run for a Synthetic test result.

    :param value: Must be one of ["scheduled", "fast", "ci", "triggered"].
    :type value: str
    """

    allowed_values = {
        "scheduled",
        "fast",
        "ci",
        "triggered",
    }
    SCHEDULED: ClassVar["SyntheticsTestResultRunType"]
    FAST: ClassVar["SyntheticsTestResultRunType"]
    CI: ClassVar["SyntheticsTestResultRunType"]
    TRIGGERED: ClassVar["SyntheticsTestResultRunType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsTestResultRunType.SCHEDULED = SyntheticsTestResultRunType("scheduled")
SyntheticsTestResultRunType.FAST = SyntheticsTestResultRunType("fast")
SyntheticsTestResultRunType.CI = SyntheticsTestResultRunType("ci")
SyntheticsTestResultRunType.TRIGGERED = SyntheticsTestResultRunType("triggered")
