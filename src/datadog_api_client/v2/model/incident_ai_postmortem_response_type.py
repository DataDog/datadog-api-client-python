# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentAIPostmortemResponseType(ModelSimple):
    """
    AI postmortem response resource type.

    :param value: If omitted defaults to "get_incident_ai_postmortem_response". Must be one of ["get_incident_ai_postmortem_response"].
    :type value: str
    """

    allowed_values = {
        "get_incident_ai_postmortem_response",
    }
    GET_INCIDENT_AI_POSTMORTEM_RESPONSE: ClassVar["IncidentAIPostmortemResponseType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentAIPostmortemResponseType.GET_INCIDENT_AI_POSTMORTEM_RESPONSE = IncidentAIPostmortemResponseType(
    "get_incident_ai_postmortem_response"
)
