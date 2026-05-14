# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_ms_teams_channel import IncidentMSTeamsChannel


class IncidentMSTeamsIntegrationDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_ms_teams_channel import IncidentMSTeamsChannel

        return {
            "created": (datetime,),
            "integration_type": (str,),
            "modified": (datetime,),
            "status": (str,),
            "teams": ([IncidentMSTeamsChannel],),
        }

    attribute_map = {
        "created": "created",
        "integration_type": "integration_type",
        "modified": "modified",
        "status": "status",
        "teams": "teams",
    }

    def __init__(
        self_,
        created: datetime,
        integration_type: str,
        modified: datetime,
        status: str,
        teams: List[IncidentMSTeamsChannel],
        **kwargs,
    ):
        """
        Attributes of a Microsoft Teams integration metadata.

        :param created: Timestamp when the integration was created.
        :type created: datetime

        :param integration_type: The type of integration.
        :type integration_type: str

        :param modified: Timestamp when the integration was last modified.
        :type modified: datetime

        :param status: The status of the integration.
        :type status: str

        :param teams: List of Microsoft Teams channels.
        :type teams: [IncidentMSTeamsChannel]
        """
        super().__init__(kwargs)

        self_.created = created
        self_.integration_type = integration_type
        self_.modified = modified
        self_.status = status
        self_.teams = teams
