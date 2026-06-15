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
    from datadog_api_client.v2.model.tag_policy_create_attributes import TagPolicyCreateAttributes
    from datadog_api_client.v2.model.tag_policy_resource_type import TagPolicyResourceType


class TagPolicyCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_policy_create_attributes import TagPolicyCreateAttributes
        from datadog_api_client.v2.model.tag_policy_resource_type import TagPolicyResourceType

        return {
            "attributes": (TagPolicyCreateAttributes,),
            "type": (TagPolicyResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: TagPolicyCreateAttributes, type: TagPolicyResourceType, **kwargs):
        """
        Data object for creating a tag policy.

        :param attributes: Attributes that can be supplied when creating a tag policy.
        :type attributes: TagPolicyCreateAttributes

        :param type: JSON:API resource type for a tag policy.
        :type type: TagPolicyResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
