# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentPageRoleType(ModelSimple):
    """
    The type of incident role for a page.

    :param value: Must be one of ["incident_user_defined_roles", "incident_reserved_roles"].
    :type value: str
    """

    allowed_values = {
        "incident_user_defined_roles",
        "incident_reserved_roles",
    }
    INCIDENT_USER_DEFINED_ROLES: ClassVar["IncidentPageRoleType"]
    INCIDENT_RESERVED_ROLES: ClassVar["IncidentPageRoleType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentPageRoleType.INCIDENT_USER_DEFINED_ROLES = IncidentPageRoleType("incident_user_defined_roles")
IncidentPageRoleType.INCIDENT_RESERVED_ROLES = IncidentPageRoleType("incident_reserved_roles")
