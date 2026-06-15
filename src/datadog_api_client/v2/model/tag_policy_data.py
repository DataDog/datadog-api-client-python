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
    from datadog_api_client.v2.model.tag_policy_attributes import TagPolicyAttributes
    from datadog_api_client.v2.model.tag_policy_relationships import TagPolicyRelationships
    from datadog_api_client.v2.model.tag_policy_resource_type import TagPolicyResourceType


class TagPolicyData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_policy_attributes import TagPolicyAttributes
        from datadog_api_client.v2.model.tag_policy_relationships import TagPolicyRelationships
        from datadog_api_client.v2.model.tag_policy_resource_type import TagPolicyResourceType

        return {
            "attributes": (TagPolicyAttributes,),
            "id": (str,),
            "relationships": (TagPolicyRelationships,),
            "type": (TagPolicyResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: TagPolicyAttributes,
        id: str,
        type: TagPolicyResourceType,
        relationships: Union[TagPolicyRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        A tag policy resource.

        :param attributes: The attributes of a tag policy resource.
        :type attributes: TagPolicyAttributes

        :param id: The unique identifier of the tag policy.
        :type id: str

        :param relationships: Related resources for a tag policy. Only present when the corresponding ``include`` query parameter is supplied.
        :type relationships: TagPolicyRelationships, optional

        :param type: JSON:API resource type for a tag policy.
        :type type: TagPolicyResourceType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
