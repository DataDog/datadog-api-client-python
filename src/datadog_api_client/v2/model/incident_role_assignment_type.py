# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentRoleAssignmentType(ModelSimple):
    """
    Incident role assignment resource type.

    :param value: If omitted defaults to "incident_role_assignments". Must be one of ["incident_role_assignments"].
    :type value: str
    """

    allowed_values = {
        "incident_role_assignments",
    }
    INCIDENT_ROLE_ASSIGNMENTS: ClassVar["IncidentRoleAssignmentType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentRoleAssignmentType.INCIDENT_ROLE_ASSIGNMENTS = IncidentRoleAssignmentType("incident_role_assignments")
