# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_postmortem_update_attributes import IncidentPostmortemUpdateAttributes
    from datadog_api_client.v2.model.incident_postmortem_type import IncidentPostmortemType


class IncidentPostmortemUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_postmortem_update_attributes import IncidentPostmortemUpdateAttributes
        from datadog_api_client.v2.model.incident_postmortem_type import IncidentPostmortemType

        return {
            "attributes": (IncidentPostmortemUpdateAttributes,),
            "id": (str,),
            "type": (IncidentPostmortemType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: IncidentPostmortemUpdateAttributes, id: str, type: IncidentPostmortemType, **kwargs
    ):
        """
        The postmortem resource for an update request.

        :param attributes: The postmortem's attributes for an update request.
        :type attributes: IncidentPostmortemUpdateAttributes

        :param id: The UUID of the postmortem.
        :type id: str

        :param type: Incident postmortem resource type.
        :type type: IncidentPostmortemType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
