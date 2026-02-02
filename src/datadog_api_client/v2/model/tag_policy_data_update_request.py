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
    from datadog_api_client.v2.model.tag_policy_attributes_update_request import TagPolicyAttributesUpdateRequest
    from datadog_api_client.v2.model.tag_policy_type import TagPolicyType


class TagPolicyDataUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_policy_attributes_update_request import TagPolicyAttributesUpdateRequest
        from datadog_api_client.v2.model.tag_policy_type import TagPolicyType

        return {
            "attributes": (TagPolicyAttributesUpdateRequest,),
            "type": (TagPolicyType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: TagPolicyAttributesUpdateRequest, type: TagPolicyType, **kwargs):
        """
        Data envelope for tag policy update request.

        :param attributes: Attributes for updating a tag policy. All fields are optional.
        :type attributes: TagPolicyAttributesUpdateRequest

        :param type: The type of the resource. The value should always be ``tag_policy``.
        :type type: TagPolicyType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
