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
    from datadog_api_client.v2.model.incident_impact_create_attributes import IncidentImpactCreateAttributes
    from datadog_api_client.v2.model.incident_impact_type import IncidentImpactType


class IncidentImpactCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_impact_create_attributes import IncidentImpactCreateAttributes
        from datadog_api_client.v2.model.incident_impact_type import IncidentImpactType

        return {
            "attributes": (IncidentImpactCreateAttributes,),
            "type": (IncidentImpactType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: IncidentImpactCreateAttributes, type: IncidentImpactType, **kwargs):
        """
        Incident impact data for a create request.

        :param attributes: The incident impact's attributes for a create request.
        :type attributes: IncidentImpactCreateAttributes

        :param type: Incident impact resource type.
        :type type: IncidentImpactType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
