# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LogFormattingIssueType(ModelSimple):
    """
    The type of the resource. The value should always be `log_formatting_issues`.

    :param value: If omitted defaults to "log_formatting_issues". Must be one of ["log_formatting_issues"].
    :type value: str
    """

    allowed_values = {
        "log_formatting_issues",
    }
    LOG_FORMATTING_ISSUES: ClassVar["LogFormattingIssueType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LogFormattingIssueType.LOG_FORMATTING_ISSUES = LogFormattingIssueType("log_formatting_issues")
