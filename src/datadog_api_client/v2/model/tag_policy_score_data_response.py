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
    from datadog_api_client.v2.model.tag_policy_score_attributes_response import TagPolicyScoreAttributesResponse
    from datadog_api_client.v2.model.tag_policy_score_type import TagPolicyScoreType


class TagPolicyScoreDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_policy_score_attributes_response import TagPolicyScoreAttributesResponse
        from datadog_api_client.v2.model.tag_policy_score_type import TagPolicyScoreType

        return {
            "attributes": (TagPolicyScoreAttributesResponse,),
            "id": (str,),
            "type": (TagPolicyScoreType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: TagPolicyScoreAttributesResponse, id: str, type: TagPolicyScoreType, **kwargs):
        """
        Data envelope for tag policy score response.

        :param attributes: Attributes of a tag policy score.
        :type attributes: TagPolicyScoreAttributesResponse

        :param id: The unique identifier of the score.
        :type id: str

        :param type: The type of the resource. The value should always be ``tag_policy_score``.
        :type type: TagPolicyScoreType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
