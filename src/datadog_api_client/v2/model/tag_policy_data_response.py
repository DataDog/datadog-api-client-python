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
    from datadog_api_client.v2.model.tag_policy_attributes_response import TagPolicyAttributesResponse
    from datadog_api_client.v2.model.tag_policy_type import TagPolicyType


class TagPolicyDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_policy_attributes_response import TagPolicyAttributesResponse
        from datadog_api_client.v2.model.tag_policy_type import TagPolicyType

        return {
            "attributes": (TagPolicyAttributesResponse,),
            "id": (str,),
            "type": (TagPolicyType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: TagPolicyAttributesResponse, id: str, type: TagPolicyType, **kwargs):
        """
        Data envelope for tag policy response.

        :param attributes: Attributes of a tag policy response.
        :type attributes: TagPolicyAttributesResponse

        :param id: The unique identifier of the tag policy.
        :type id: str

        :param type: The type of the resource. The value should always be ``tag_policy``.
        :type type: TagPolicyType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
