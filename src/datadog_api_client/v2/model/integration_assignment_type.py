# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IntegrationAssignmentType(ModelSimple):
    """
    Integration assignment resource type.

    :param value: If omitted defaults to "issue_assignment". Must be one of ["issue_assignment"].
    :type value: str
    """

    allowed_values = {
        "issue_assignment",
    }
    ISSUE_ASSIGNMENT: ClassVar["IntegrationAssignmentType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IntegrationAssignmentType.ISSUE_ASSIGNMENT = IntegrationAssignmentType("issue_assignment")
