# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentMicrosoftTeamsConfigurationType(ModelSimple):
    """
    Microsoft Teams configuration resource type.

    :param value: If omitted defaults to "microsoft_teams_configurations". Must be one of ["microsoft_teams_configurations"].
    :type value: str
    """

    allowed_values = {
        "microsoft_teams_configurations",
    }
    MICROSOFT_TEAMS_CONFIGURATIONS: ClassVar["IncidentMicrosoftTeamsConfigurationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentMicrosoftTeamsConfigurationType.MICROSOFT_TEAMS_CONFIGURATIONS = IncidentMicrosoftTeamsConfigurationType(
    "microsoft_teams_configurations"
)
