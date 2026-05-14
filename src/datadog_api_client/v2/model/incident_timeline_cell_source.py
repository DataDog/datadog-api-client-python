# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentTimelineCellSource(ModelSimple):
    """
    The source of a timeline cell.

    :param value: Must be one of ["slack", "microsoft_teams", "datadog", "api"].
    :type value: str
    """

    allowed_values = {
        "slack",
        "microsoft_teams",
        "datadog",
        "api",
    }
    SLACK: ClassVar["IncidentTimelineCellSource"]
    MICROSOFT_TEAMS: ClassVar["IncidentTimelineCellSource"]
    DATADOG: ClassVar["IncidentTimelineCellSource"]
    API: ClassVar["IncidentTimelineCellSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentTimelineCellSource.SLACK = IncidentTimelineCellSource("slack")
IncidentTimelineCellSource.MICROSOFT_TEAMS = IncidentTimelineCellSource("microsoft_teams")
IncidentTimelineCellSource.DATADOG = IncidentTimelineCellSource("datadog")
IncidentTimelineCellSource.API = IncidentTimelineCellSource("api")
