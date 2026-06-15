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
    from datadog_api_client.v2.model.tag_policy_update_attributes import TagPolicyUpdateAttributes
    from datadog_api_client.v2.model.tag_policy_resource_type import TagPolicyResourceType


class TagPolicyUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_policy_update_attributes import TagPolicyUpdateAttributes
        from datadog_api_client.v2.model.tag_policy_resource_type import TagPolicyResourceType

        return {
            "attributes": (TagPolicyUpdateAttributes,),
            "id": (str,),
            "type": (TagPolicyResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: TagPolicyResourceType,
        attributes: Union[TagPolicyUpdateAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for updating a tag policy.

        :param attributes: Mutable attributes of a tag policy. Each field is optional; omitting a field leaves its
            current value unchanged. The ``source`` of a policy cannot be changed.
        :type attributes: TagPolicyUpdateAttributes, optional

        :param id: The unique identifier of the tag policy being updated.
        :type id: str

        :param type: JSON:API resource type for a tag policy.
        :type type: TagPolicyResourceType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
