# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TagRuleScoreResourceType(ModelSimple):
    """
    JSON:API resource type for a tag rule compliance score. Responses use the legacy `tag_policy_score` value.

    :param value: Must be one of ["tag_rule_score", "tag_policy_score"].
    :type value: str
    """

    allowed_values = {
        "tag_rule_score",
        "tag_policy_score",
    }
    TAG_RULE_SCORE: ClassVar["TagRuleScoreResourceType"]
    TAG_POLICY_SCORE: ClassVar["TagRuleScoreResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TagRuleScoreResourceType.TAG_RULE_SCORE = TagRuleScoreResourceType("tag_rule_score")
TagRuleScoreResourceType.TAG_POLICY_SCORE = TagRuleScoreResourceType("tag_policy_score")
