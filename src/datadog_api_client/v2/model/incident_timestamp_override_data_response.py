# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_timestamp_override_data_attributes_response import (
        IncidentTimestampOverrideDataAttributesResponse,
    )
    from datadog_api_client.v2.model.incident_timestamp_override_relationships import (
        IncidentTimestampOverrideRelationships,
    )
    from datadog_api_client.v2.model.incident_timestamp_override_type import IncidentTimestampOverrideType


class IncidentTimestampOverrideDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_timestamp_override_data_attributes_response import (
            IncidentTimestampOverrideDataAttributesResponse,
        )
        from datadog_api_client.v2.model.incident_timestamp_override_relationships import (
            IncidentTimestampOverrideRelationships,
        )
        from datadog_api_client.v2.model.incident_timestamp_override_type import IncidentTimestampOverrideType

        return {
            "attributes": (IncidentTimestampOverrideDataAttributesResponse,),
            "id": (UUID,),
            "relationships": (IncidentTimestampOverrideRelationships,),
            "type": (IncidentTimestampOverrideType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentTimestampOverrideDataAttributesResponse,
        id: UUID,
        type: IncidentTimestampOverrideType,
        relationships: Union[IncidentTimestampOverrideRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Timestamp override data in a response.

        :param attributes: Attributes of a timestamp override in a response.
        :type attributes: IncidentTimestampOverrideDataAttributesResponse

        :param id: The timestamp override identifier.
        :type id: UUID

        :param relationships: Relationships for a timestamp override.
        :type relationships: IncidentTimestampOverrideRelationships, optional

        :param type: Incident timestamp override resource type.
        :type type: IncidentTimestampOverrideType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
