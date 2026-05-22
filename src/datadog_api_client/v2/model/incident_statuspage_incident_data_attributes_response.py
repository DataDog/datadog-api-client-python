# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_statuspage_incident_entry import IncidentStatuspageIncidentEntry


class IncidentStatuspageIncidentDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_statuspage_incident_entry import IncidentStatuspageIncidentEntry

        return {
            "created": (datetime,),
            "incidents": ([IncidentStatuspageIncidentEntry],),
            "integration_type": (str,),
            "modified": (datetime,),
            "status": (str,),
        }

    attribute_map = {
        "created": "created",
        "incidents": "incidents",
        "integration_type": "integration_type",
        "modified": "modified",
        "status": "status",
    }

    def __init__(
        self_,
        created: datetime,
        integration_type: str,
        modified: datetime,
        status: str,
        incidents: Union[List[IncidentStatuspageIncidentEntry], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a Statuspage incident integration.

        :param created: Timestamp when the integration was created.
        :type created: datetime

        :param incidents: List of Statuspage incidents.
        :type incidents: [IncidentStatuspageIncidentEntry], optional

        :param integration_type: The type of integration.
        :type integration_type: str

        :param modified: Timestamp when the integration was last modified.
        :type modified: datetime

        :param status: The status of the integration.
        :type status: str
        """
        if incidents is not unset:
            kwargs["incidents"] = incidents
        super().__init__(kwargs)

        self_.created = created
        self_.integration_type = integration_type
        self_.modified = modified
        self_.status = status
