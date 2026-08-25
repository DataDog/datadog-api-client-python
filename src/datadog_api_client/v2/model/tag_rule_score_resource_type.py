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
    JSON:API resource type for a tag rule compliance score.

    :param value: If omitted defaults to "tag_rule_score". Must be one of ["tag_rule_score"].
    :type value: str
    """

    allowed_values = {
        "tag_rule_score",
    }
    TAG_RULE_SCORE: ClassVar["TagRuleScoreResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TagRuleScoreResourceType.TAG_RULE_SCORE = TagRuleScoreResourceType("tag_rule_score")
