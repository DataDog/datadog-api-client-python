# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentOrgSettingsType(ModelSimple):
    """
    Incident org settings resource type.

    :param value: If omitted defaults to "incident_org_settings". Must be one of ["incident_org_settings"].
    :type value: str
    """

    allowed_values = {
        "incident_org_settings",
    }
    INCIDENT_ORG_SETTINGS: ClassVar["IncidentOrgSettingsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentOrgSettingsType.INCIDENT_ORG_SETTINGS = IncidentOrgSettingsType("incident_org_settings")
