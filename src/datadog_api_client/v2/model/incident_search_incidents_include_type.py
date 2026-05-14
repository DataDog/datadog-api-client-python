# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentSearchIncidentsIncludeType(ModelSimple):
    """
    Types of related objects to include.

    :param value: Must be one of ["incident_type", "impacts", "users", "responders", "integrations", "attachments"].
    :type value: str
    """

    allowed_values = {
        "incident_type",
        "impacts",
        "users",
        "responders",
        "integrations",
        "attachments",
    }
    INCIDENT_TYPE: ClassVar["IncidentSearchIncidentsIncludeType"]
    IMPACTS: ClassVar["IncidentSearchIncidentsIncludeType"]
    USERS: ClassVar["IncidentSearchIncidentsIncludeType"]
    RESPONDERS: ClassVar["IncidentSearchIncidentsIncludeType"]
    INTEGRATIONS: ClassVar["IncidentSearchIncidentsIncludeType"]
    ATTACHMENTS: ClassVar["IncidentSearchIncidentsIncludeType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentSearchIncidentsIncludeType.INCIDENT_TYPE = IncidentSearchIncidentsIncludeType("incident_type")
IncidentSearchIncidentsIncludeType.IMPACTS = IncidentSearchIncidentsIncludeType("impacts")
IncidentSearchIncidentsIncludeType.USERS = IncidentSearchIncidentsIncludeType("users")
IncidentSearchIncidentsIncludeType.RESPONDERS = IncidentSearchIncidentsIncludeType("responders")
IncidentSearchIncidentsIncludeType.INTEGRATIONS = IncidentSearchIncidentsIncludeType("integrations")
IncidentSearchIncidentsIncludeType.ATTACHMENTS = IncidentSearchIncidentsIncludeType("attachments")
