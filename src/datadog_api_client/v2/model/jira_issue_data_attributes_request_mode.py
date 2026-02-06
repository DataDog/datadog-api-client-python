# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class JiraIssueDataAttributesRequestMode(ModelSimple):
    """
    Mode for creating the Jira issue. Can be "single" or "multiple".

    :param value: Must be one of ["single", "multiple"].
    :type value: str
    """

    allowed_values = {
        "single",
        "multiple",
    }
    SINGLE: ClassVar["JiraIssueDataAttributesRequestMode"]
    MULTIPLE: ClassVar["JiraIssueDataAttributesRequestMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


JiraIssueDataAttributesRequestMode.SINGLE = JiraIssueDataAttributesRequestMode("single")
JiraIssueDataAttributesRequestMode.MULTIPLE = JiraIssueDataAttributesRequestMode("multiple")
