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
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.team_reference_attributes import TeamReferenceAttributes
    from datadog_api_client.v2.model.team_reference_relationships import TeamReferenceRelationships
    from datadog_api_client.v2.model.team_reference_type import TeamReferenceType


class TeamReference(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_reference_attributes import TeamReferenceAttributes
        from datadog_api_client.v2.model.team_reference_relationships import TeamReferenceRelationships
        from datadog_api_client.v2.model.team_reference_type import TeamReferenceType

        return {
            "attributes": (TeamReferenceAttributes,),
            "id": (str,),
            "relationships": (TeamReferenceRelationships,),
            "type": (TeamReferenceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[TeamReferenceAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[TeamReferenceRelationships, UnsetType] = unset,
        type: Union[TeamReferenceType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Provides a reference to a team, including ID, type, and basic attributes/relationships.

        :param attributes: Encapsulates the basic attributes of a Team reference, such as name, handle, and an optional avatar or description.
        :type attributes: TeamReferenceAttributes, optional

        :param id: The team's unique identifier.
        :type id: str, optional

        :param relationships: Collects the key relationship fields for a team reference, specifically on-call users.
        :type relationships: TeamReferenceRelationships, optional

        :param type: Teams resource type.
        :type type: TeamReferenceType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
