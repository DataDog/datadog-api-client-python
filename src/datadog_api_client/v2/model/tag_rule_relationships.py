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
    from datadog_api_client.v2.model.tag_rule_score_relationship import TagRuleScoreRelationship


class TagRuleRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_rule_score_relationship import TagRuleScoreRelationship

        return {
            "score": (TagRuleScoreRelationship,),
        }

    attribute_map = {
        "score": "score",
    }

    def __init__(self_, score: Union[TagRuleScoreRelationship, UnsetType] = unset, **kwargs):
        """
        Related resources for a tag rule. Only present when the corresponding ``include`` query parameter is supplied.

        :param score: A relationship to the compliance score resource for this rule.
        :type score: TagRuleScoreRelationship, optional
        """
        if score is not unset:
            kwargs["score"] = score
        super().__init__(kwargs)
