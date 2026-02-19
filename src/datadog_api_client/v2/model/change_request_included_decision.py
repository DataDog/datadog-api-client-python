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
    from datadog_api_client.v2.model.change_request_decision_response_attributes import (
        ChangeRequestDecisionResponseAttributes,
    )
    from datadog_api_client.v2.model.change_request_decision_relationships import ChangeRequestDecisionRelationships
    from datadog_api_client.v2.model.change_request_decision_resource_type import ChangeRequestDecisionResourceType


class ChangeRequestIncludedDecision(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.change_request_decision_response_attributes import (
            ChangeRequestDecisionResponseAttributes,
        )
        from datadog_api_client.v2.model.change_request_decision_relationships import ChangeRequestDecisionRelationships
        from datadog_api_client.v2.model.change_request_decision_resource_type import ChangeRequestDecisionResourceType

        return {
            "attributes": (ChangeRequestDecisionResponseAttributes,),
            "id": (str,),
            "relationships": (ChangeRequestDecisionRelationships,),
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
        attributes: ChangeRequestDecisionResponseAttributes,
        id: str,
        type: ChangeRequestDecisionResourceType,
        relationships: Union[ChangeRequestDecisionRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        An included change request decision resource.

        :param attributes: Attributes of a change request decision in a response.
        :type attributes: ChangeRequestDecisionResponseAttributes

        :param id: The decision UUID.
        :type id: str

        :param relationships: Relationships of a change request decision.
        :type relationships: ChangeRequestDecisionRelationships, optional

        :param type: Change request decision resource type.
        :type type: ChangeRequestDecisionResourceType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
