# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LogsIssueStreamQueryDataSource(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: If omitted defaults to "logs_issue_stream". Must be one of ["logs_issue_stream"].
    :type value: str
    """

    allowed_values = {
        "logs_issue_stream",
    }
    LOGS_ISSUE_STREAM: ClassVar["LogsIssueStreamQueryDataSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LogsIssueStreamQueryDataSource.LOGS_ISSUE_STREAM = LogsIssueStreamQueryDataSource("logs_issue_stream")
