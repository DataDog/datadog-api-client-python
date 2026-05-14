# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentStatusPagesSuggestionType(ModelSimple):
    """
    Incident status pages suggestion resource type.

    :param value: If omitted defaults to "incident_statuspages_suggestion". Must be one of ["incident_statuspages_suggestion"].
    :type value: str
    """

    allowed_values = {
        "incident_statuspages_suggestion",
    }
    INCIDENT_STATUSPAGES_SUGGESTION: ClassVar["IncidentStatusPagesSuggestionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentStatusPagesSuggestionType.INCIDENT_STATUSPAGES_SUGGESTION = IncidentStatusPagesSuggestionType(
    "incident_statuspages_suggestion"
)
