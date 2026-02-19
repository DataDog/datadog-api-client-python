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
    from datadog_api_client.v2.model.change_request_decision_update_data_attributes import (
        ChangeRequestDecisionUpdateDataAttributes,
    )
    from datadog_api_client.v2.model.change_request_decision_update_data_relationships import (
        ChangeRequestDecisionUpdateDataRelationships,
    )
    from datadog_api_client.v2.model.change_request_resource_type import ChangeRequestResourceType


class ChangeRequestDecisionUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.change_request_decision_update_data_attributes import (
            ChangeRequestDecisionUpdateDataAttributes,
        )
        from datadog_api_client.v2.model.change_request_decision_update_data_relationships import (
            ChangeRequestDecisionUpdateDataRelationships,
        )
        from datadog_api_client.v2.model.change_request_resource_type import ChangeRequestResourceType

        return {
            "attributes": (ChangeRequestDecisionUpdateDataAttributes,),
            "relationships": (ChangeRequestDecisionUpdateDataRelationships,),
            "type": (ChangeRequestResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        type: ChangeRequestResourceType,
        attributes: Union[ChangeRequestDecisionUpdateDataAttributes, UnsetType] = unset,
        relationships: Union[ChangeRequestDecisionUpdateDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object to update a change request decision.

        :param attributes: Attributes of the parent change request for a decision update.
        :type attributes: ChangeRequestDecisionUpdateDataAttributes, optional

        :param relationships: Relationships for updating a change request decision.
        :type relationships: ChangeRequestDecisionUpdateDataRelationships, optional

        :param type: Change request resource type.
        :type type: ChangeRequestResourceType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
