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
    from datadog_api_client.v2.model.tag_rule_score_relationship_data import TagRuleScoreRelationshipData


class TagRuleScoreRelationship(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_rule_score_relationship_data import TagRuleScoreRelationshipData

        return {
            "data": (TagRuleScoreRelationshipData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: TagRuleScoreRelationshipData, **kwargs):
        """
        A relationship to the compliance score resource for this rule.

        :param data: Identifier of the related compliance score resource.
        :type data: TagRuleScoreRelationshipData
        """
        super().__init__(kwargs)

        self_.data = data
