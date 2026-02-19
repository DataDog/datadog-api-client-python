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
    from datadog_api_client.v2.model.change_request_update_attributes import ChangeRequestUpdateAttributes
    from datadog_api_client.v2.model.change_request_update_relationships import ChangeRequestUpdateRelationships
    from datadog_api_client.v2.model.change_request_resource_type import ChangeRequestResourceType


class ChangeRequestUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.change_request_update_attributes import ChangeRequestUpdateAttributes
        from datadog_api_client.v2.model.change_request_update_relationships import ChangeRequestUpdateRelationships
        from datadog_api_client.v2.model.change_request_resource_type import ChangeRequestResourceType

        return {
            "attributes": (ChangeRequestUpdateAttributes,),
            "relationships": (ChangeRequestUpdateRelationships,),
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
        attributes: Union[ChangeRequestUpdateAttributes, UnsetType] = unset,
        relationships: Union[ChangeRequestUpdateRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object to update a change request.

        :param attributes: Attributes for updating a change request.
        :type attributes: ChangeRequestUpdateAttributes, optional

        :param relationships: Relationships for updating a change request.
        :type relationships: ChangeRequestUpdateRelationships, optional

        :param type: Change request resource type.
        :type type: ChangeRequestResourceType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
