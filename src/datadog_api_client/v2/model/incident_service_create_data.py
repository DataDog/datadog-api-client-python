# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.incident_service_create_attributes import IncidentServiceCreateAttributes

if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_service_relationships import IncidentServiceRelationships
    from datadog_api_client.v2.model.incident_service_type import IncidentServiceType


@dataclass
class IncidentServiceCreateDataJSON:
    name: Union[str, UnsetType] = unset
    created_by: Union[str, UnsetType] = unset
    last_modified_by: Union[str, UnsetType] = unset


class IncidentServiceCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_service_relationships import IncidentServiceRelationships
        from datadog_api_client.v2.model.incident_service_type import IncidentServiceType

        return {
            "attributes": (IncidentServiceCreateAttributes,),
            "relationships": (IncidentServiceRelationships,),
            "type": (IncidentServiceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }
    read_only_vars = {
        "relationships",
    }
    json_api_model = IncidentServiceCreateDataJSON

    def __init__(
        self_,
        type: IncidentServiceType,
        attributes: Union[IncidentServiceCreateAttributes, UnsetType] = unset,
        relationships: Union[IncidentServiceRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Incident Service payload for create requests.

        :param attributes: The incident service's attributes for a create request.
        :type attributes: IncidentServiceCreateAttributes, optional

        :param relationships: The incident service's relationships.
        :type relationships: IncidentServiceRelationships, optional

        :param type: Incident service resource type.
        :type type: IncidentServiceType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
