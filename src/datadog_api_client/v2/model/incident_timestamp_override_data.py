# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_timestamp_override_attributes import IncidentTimestampOverrideAttributes
    from datadog_api_client.v2.model.incident_timestamp_override_relationships import (
        IncidentTimestampOverrideRelationships,
    )
    from datadog_api_client.v2.model.incidents_timestamp_overrides_type import IncidentsTimestampOverridesType


class IncidentTimestampOverrideData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_timestamp_override_attributes import (
            IncidentTimestampOverrideAttributes,
        )
        from datadog_api_client.v2.model.incident_timestamp_override_relationships import (
            IncidentTimestampOverrideRelationships,
        )
        from datadog_api_client.v2.model.incidents_timestamp_overrides_type import IncidentsTimestampOverridesType

        return {
            "attributes": (IncidentTimestampOverrideAttributes,),
            "id": (UUID,),
            "relationships": (IncidentTimestampOverrideRelationships,),
            "type": (IncidentsTimestampOverridesType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentTimestampOverrideAttributes,
        id: UUID,
        relationships: IncidentTimestampOverrideRelationships,
        type: IncidentsTimestampOverridesType,
        **kwargs,
    ):
        """
        Data for a single incident timestamp override.

        :param attributes: Attributes of an incident timestamp override.
        :type attributes: IncidentTimestampOverrideAttributes

        :param id: The UUID of the timestamp override.
        :type id: UUID

        :param relationships: Relationships for incident timestamp override.
        :type relationships: IncidentTimestampOverrideRelationships

        :param type: The JSON:API type for timestamp overrides.
        :type type: IncidentsTimestampOverridesType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.relationships = relationships
        self_.type = type
