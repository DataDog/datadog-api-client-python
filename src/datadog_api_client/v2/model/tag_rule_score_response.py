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
    from datadog_api_client.v2.model.tag_rule_score_data import TagRuleScoreData


class TagRuleScoreResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_rule_score_data import TagRuleScoreData

        return {
            "data": (TagRuleScoreData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: TagRuleScoreData, **kwargs):
        """
        A tag rule compliance score.

        :param data: A compliance score resource for a tag rule.
        :type data: TagRuleScoreData
        """
        super().__init__(kwargs)

        self_.data = data
