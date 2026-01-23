# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ServiceNowAssignmentGroupType(ModelSimple):
    """
    Type identifier for ServiceNow assignment group resources

    :param value: If omitted defaults to "assignment_groups". Must be one of ["assignment_groups"].
    :type value: str
    """

    allowed_values = {
        "assignment_groups",
    }
    ASSIGNMENT_GROUPS: ClassVar["ServiceNowAssignmentGroupType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ServiceNowAssignmentGroupType.ASSIGNMENT_GROUPS = ServiceNowAssignmentGroupType("assignment_groups")
