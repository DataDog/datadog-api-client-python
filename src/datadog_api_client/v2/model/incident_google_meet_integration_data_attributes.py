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
    from datadog_api_client.v2.model.incident_google_meet_space import IncidentGoogleMeetSpace


class IncidentGoogleMeetIntegrationDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_google_meet_space import IncidentGoogleMeetSpace

        return {
            "created": (datetime,),
            "integration_type": (str,),
            "modified": (datetime,),
            "spaces": ([IncidentGoogleMeetSpace],),
            "status": (str,),
        }

    attribute_map = {
        "created": "created",
        "integration_type": "integration_type",
        "modified": "modified",
        "spaces": "spaces",
        "status": "status",
    }

    def __init__(
        self_,
        created: datetime,
        integration_type: str,
        modified: datetime,
        spaces: List[IncidentGoogleMeetSpace],
        status: str,
        **kwargs,
    ):
        """
        Attributes of a Google Meet integration metadata.

        :param created: Timestamp when the integration was created.
        :type created: datetime

        :param integration_type: The type of integration.
        :type integration_type: str

        :param modified: Timestamp when the integration was last modified.
        :type modified: datetime

        :param spaces: List of Google Meet spaces.
        :type spaces: [IncidentGoogleMeetSpace]

        :param status: The status of the integration.
        :type status: str
        """
        super().__init__(kwargs)

        self_.created = created
        self_.integration_type = integration_type
        self_.modified = modified
        self_.spaces = spaces
        self_.status = status
