# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsTestResultStatus(ModelSimple):
    """
    Status of a Synthetic test result.

    :param value: Must be one of ["passed", "failed", "no_data"].
    :type value: str
    """

    allowed_values = {
        "passed",
        "failed",
        "no_data",
    }
    PASSED: ClassVar["SyntheticsTestResultStatus"]
    FAILED: ClassVar["SyntheticsTestResultStatus"]
    NO_DATA: ClassVar["SyntheticsTestResultStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsTestResultStatus.PASSED = SyntheticsTestResultStatus("passed")
SyntheticsTestResultStatus.FAILED = SyntheticsTestResultStatus("failed")
SyntheticsTestResultStatus.NO_DATA = SyntheticsTestResultStatus("no_data")
