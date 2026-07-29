# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentRuleTriggerType(ModelSimple):
    """
    The trigger event for an incident rule.

    :param value: Must be one of ["incident_saved_trigger", "incident_created_trigger", "incident_modified_trigger"].
    :type value: str
    """

    allowed_values = {
        "incident_saved_trigger",
        "incident_created_trigger",
        "incident_modified_trigger",
    }
    INCIDENT_SAVED_TRIGGER: ClassVar["IncidentRuleTriggerType"]
    INCIDENT_CREATED_TRIGGER: ClassVar["IncidentRuleTriggerType"]
    INCIDENT_MODIFIED_TRIGGER: ClassVar["IncidentRuleTriggerType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentRuleTriggerType.INCIDENT_SAVED_TRIGGER = IncidentRuleTriggerType("incident_saved_trigger")
IncidentRuleTriggerType.INCIDENT_CREATED_TRIGGER = IncidentRuleTriggerType("incident_created_trigger")
IncidentRuleTriggerType.INCIDENT_MODIFIED_TRIGGER = IncidentRuleTriggerType("incident_modified_trigger")
