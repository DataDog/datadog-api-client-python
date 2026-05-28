# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IssueDefinitionDataType(ModelSimple):
    """
    Issue definitions resource type.

    :param value: If omitted defaults to "issue_definitions". Must be one of ["issue_definitions"].
    :type value: str
    """

    allowed_values = {
        "issue_definitions",
    }
    ISSUE_DEFINITIONS: ClassVar["IssueDefinitionDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IssueDefinitionDataType.ISSUE_DEFINITIONS = IssueDefinitionDataType("issue_definitions")
