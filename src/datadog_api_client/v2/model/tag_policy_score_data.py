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
    from datadog_api_client.v2.model.tag_policy_score_attributes import TagPolicyScoreAttributes
    from datadog_api_client.v2.model.tag_policy_score_resource_type import TagPolicyScoreResourceType


class TagPolicyScoreData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_policy_score_attributes import TagPolicyScoreAttributes
        from datadog_api_client.v2.model.tag_policy_score_resource_type import TagPolicyScoreResourceType

        return {
            "attributes": (TagPolicyScoreAttributes,),
            "id": (str,),
            "type": (TagPolicyScoreResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: TagPolicyScoreAttributes, id: str, type: TagPolicyScoreResourceType, **kwargs):
        """
        A compliance score resource for a tag policy.

        :param attributes: Attributes of a tag policy compliance score.
        :type attributes: TagPolicyScoreAttributes

        :param id: The unique identifier of the compliance score resource.
        :type id: str

        :param type: JSON:API resource type for a tag policy compliance score.
        :type type: TagPolicyScoreResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
