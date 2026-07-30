# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentServiceNowRecordPromptType(ModelSimple):
    """
    ServiceNow record prompt resource type.

    :param value: If omitted defaults to "incident_servicenow_record_prompt". Must be one of ["incident_servicenow_record_prompt"].
    :type value: str
    """

    allowed_values = {
        "incident_servicenow_record_prompt",
    }
    INCIDENT_SERVICENOW_RECORD_PROMPT: ClassVar["IncidentServiceNowRecordPromptType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentServiceNowRecordPromptType.INCIDENT_SERVICENOW_RECORD_PROMPT = IncidentServiceNowRecordPromptType(
    "incident_servicenow_record_prompt"
)
