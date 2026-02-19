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
    from datadog_api_client.v2.model.change_request_decision_create_attributes import (
        ChangeRequestDecisionCreateAttributes,
    )
    from datadog_api_client.v2.model.change_request_decision_create_relationships import (
        ChangeRequestDecisionCreateRelationships,
    )
    from datadog_api_client.v2.model.change_request_decision_resource_type import ChangeRequestDecisionResourceType


class ChangeRequestDecisionCreateItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.change_request_decision_create_attributes import (
            ChangeRequestDecisionCreateAttributes,
        )
        from datadog_api_client.v2.model.change_request_decision_create_relationships import (
            ChangeRequestDecisionCreateRelationships,
        )
        from datadog_api_client.v2.model.change_request_decision_resource_type import ChangeRequestDecisionResourceType

        return {
            "attributes": (ChangeRequestDecisionCreateAttributes,),
            "id": (str,),
            "relationships": (ChangeRequestDecisionCreateRelationships,),
            "type": (ChangeRequestDecisionResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: ChangeRequestDecisionResourceType,
        attributes: Union[ChangeRequestDecisionCreateAttributes, UnsetType] = unset,
        relationships: Union[ChangeRequestDecisionCreateRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        An included change request decision for a create or update operation.

        :param attributes: Attributes for creating a change request decision.
        :type attributes: ChangeRequestDecisionCreateAttributes, optional

        :param id: The decision identifier.
        :type id: str

        :param relationships: Relationships for creating a change request decision.
        :type relationships: ChangeRequestDecisionCreateRelationships, optional

        :param type: Change request decision resource type.
        :type type: ChangeRequestDecisionResourceType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
